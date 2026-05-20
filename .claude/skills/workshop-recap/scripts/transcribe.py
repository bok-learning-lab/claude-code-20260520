#!/usr/bin/env python3
"""
transcribe.py - Transcribe a large audio or video file with the OpenAI Whisper API.

The Whisper API rejects any file larger than 25 MB, and workshop recordings are
far bigger than that. This script uses ffmpeg to split the input into small mono
chunks, transcribes each chunk with the `whisper-1` model, and joins the results
into a single plain-text transcript.

Usage:
    python3 transcribe.py INPUT [options]

Options:
    -o, --output PATH     Where to write the transcript. Default: next to INPUT,
                          with a trailing "_audio" replaced by "_transcript"
                          (otherwise "_transcript" is appended), ending in .txt.
    --force               Re-transcribe even if the output file already exists.
    --chunk-minutes N     Minutes of audio per chunk (default: 10).
    --workers N           Number of parallel API calls (default: 4).
    --language CODE       ISO-639-1 language hint, e.g. "en" (default: en).
    --prompt TEXT         Spelling / vocabulary hint passed to Whisper.
    --keep-temp           Keep the temporary chunk files (for debugging).

Requirements:
    - ffmpeg and ffprobe on PATH        (brew install ffmpeg)
    - the `openai` Python package       (pip3 install openai)
    - an OpenAI API key, read from the OPENAI_API_KEY environment variable, or
      from an .env.local file in the working directory or any parent directory.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

WHISPER_MODEL = "whisper-1"
SAFE_CHUNK_LIMIT = 24 * 1024 * 1024  # stay just under the API's 25 MB limit
COST_PER_MINUTE = 0.006              # Whisper API pricing, for a rough estimate
DEFAULT_PROMPT = (
    "A workshop about Claude, Claude Code, Claude Cowork, Anthropic, "
    "Harvard, and HUIT."
)


def die(msg: str) -> None:
    """Print an error and exit. (Raised inside a worker thread, this still
    surfaces the message and exits cleanly with a non-zero status.)"""
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)


def load_api_key() -> str:
    """Find the OpenAI API key: env var first, then an .env.local file in the
    current directory or any parent."""
    key = os.environ.get("OPENAI_API_KEY")
    if key and key.strip():
        return key.strip()

    here = Path.cwd()
    for folder in [here, *here.parents]:
        env_file = folder / ".env.local"
        if not env_file.is_file():
            continue
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            name, _, value = line.partition("=")
            if name.strip() == "OPENAI_API_KEY":
                return value.strip().strip('"').strip("'")

    die("no OPENAI_API_KEY found - set the env var, or add it to an .env.local file")
    return ""  # unreachable, keeps type checkers happy


def audio_duration(path: Path) -> float:
    """Return the duration of an audio/video file in seconds, via ffprobe."""
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        capture_output=True, text=True,
    )
    try:
        return float(result.stdout.strip())
    except ValueError:
        die(f"could not read the audio duration of {path}")
        return 0.0  # unreachable


def split_into_chunks(src: Path, chunk_seconds: int, workdir: Path) -> list:
    """Re-encode the input to small mono MP3 chunks with ffmpeg. Dropping the
    video stream and downmixing to 16 kHz mono keeps every chunk tiny while
    losing nothing Whisper uses (it works at 16 kHz internally)."""
    pattern = str(workdir / "chunk_%03d.mp3")
    cmd = [
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(src),
        "-vn",                                  # drop any video stream
        "-ac", "1",                             # mono
        "-ar", "16000",                         # 16 kHz
        "-c:a", "libmp3lame", "-b:a", "64k",    # ~0.48 MB per minute
        "-f", "segment",
        "-segment_time", str(chunk_seconds),
        "-reset_timestamps", "1",
        pattern,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        die(f"ffmpeg failed:\n{result.stderr.strip()}")

    chunks = sorted(workdir.glob("chunk_*.mp3"))
    if not chunks:
        die("ffmpeg produced no chunks - is the input a valid media file?")
    for chunk in chunks:
        size = chunk.stat().st_size
        if size > SAFE_CHUNK_LIMIT:
            die(f"{chunk.name} is {size / 1e6:.1f} MB, over the API limit - "
                f"re-run with a smaller --chunk-minutes")
    return chunks


def transcribe_chunk(client, chunk: Path, language: str, prompt: str) -> str:
    """Transcribe one chunk, retrying a few times on transient errors."""
    last_error = None
    for attempt in range(1, 4):
        try:
            with open(chunk, "rb") as handle:
                kwargs = {
                    "model": WHISPER_MODEL,
                    "file": handle,
                    "response_format": "text",
                }
                if language:
                    kwargs["language"] = language
                if prompt:
                    kwargs["prompt"] = prompt
                text = client.audio.transcriptions.create(**kwargs)
            return str(text).strip()
        except Exception as error:  # surface any API/network failure
            last_error = error
            wait = 2 ** attempt
            print(f"  {chunk.name}: attempt {attempt} failed ({error}); "
                  f"retrying in {wait}s", file=sys.stderr)
            time.sleep(wait)
    die(f"{chunk.name}: giving up after 3 attempts ({last_error})")
    return ""  # unreachable


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Transcribe a large audio/video file with the Whisper API.")
    parser.add_argument("input", help="audio or video file to transcribe")
    parser.add_argument("-o", "--output", help="output transcript path (.txt)")
    parser.add_argument("--force", action="store_true",
                        help="overwrite an existing transcript")
    parser.add_argument("--chunk-minutes", type=float, default=10.0,
                        help="minutes of audio per chunk (default: 10)")
    parser.add_argument("--workers", type=int, default=4,
                        help="parallel API calls (default: 4)")
    parser.add_argument("--language", default="en",
                        help="ISO-639-1 language hint (default: en)")
    parser.add_argument("--prompt", default=DEFAULT_PROMPT,
                        help="spelling/vocabulary hint passed to Whisper")
    parser.add_argument("--keep-temp", action="store_true",
                        help="keep the temporary chunk files")
    args = parser.parse_args()

    src = Path(args.input).expanduser().resolve()
    if not src.is_file():
        die(f"input file not found: {src}")

    if args.output:
        out_path = Path(args.output).expanduser().resolve()
    else:
        stem = src.stem
        if stem.endswith("_audio"):
            stem = stem[:-len("_audio")] + "_transcript"
        else:
            stem = stem + "_transcript"
        out_path = src.with_name(stem + ".txt")

    if out_path.exists() and not args.force:
        print(f"transcript already exists: {out_path}")
        print("(pass --force to re-transcribe)")
        return

    for tool in ("ffmpeg", "ffprobe"):
        if shutil.which(tool) is None:
            die(f"{tool} not found on PATH - install it with: brew install ffmpeg")

    try:
        from openai import OpenAI
    except ImportError:
        die("the `openai` package is not installed - run: pip3 install openai")
        return

    client = OpenAI(api_key=load_api_key(), timeout=600.0)

    duration = audio_duration(src)
    chunk_seconds = max(60, int(args.chunk_minutes * 60))
    print(f"input:    {src}")
    print(f"duration: {duration / 60:.1f} min")
    print(f"estimate: ~${duration / 60 * COST_PER_MINUTE:.2f} "
          f"(Whisper API, ${COST_PER_MINUTE}/min)")
    print(f"splitting into ~{chunk_seconds // 60}-minute chunks ...")

    workdir = Path(tempfile.mkdtemp(prefix="transcribe_"))
    try:
        chunks = split_into_chunks(src, chunk_seconds, workdir)
        print(f"transcribing {len(chunks)} chunk(s) with {WHISPER_MODEL}, "
              f"{args.workers} at a time ...")

        results = [""] * len(chunks)
        done = 0

        def work(item):
            index, chunk = item
            return index, transcribe_chunk(client, chunk, args.language, args.prompt)

        with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
            for index, text in pool.map(work, list(enumerate(chunks))):
                results[index] = text
                done += 1
                print(f"  [{done}/{len(chunks)}] chunk {index + 1} done")

        transcript = " ".join(part for part in results if part).strip() + "\n"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(transcript, encoding="utf-8")
        print(f"\ndone - {len(transcript.split()):,} words written to:\n{out_path}")
    finally:
        if args.keep_temp:
            print(f"(temporary chunks kept in {workdir})")
        else:
            shutil.rmtree(workdir, ignore_errors=True)


if __name__ == "__main__":
    main()
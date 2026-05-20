---
name: workshop-recap
description: Transcribe a workshop or lecture day's audio/video recording and turn it into a beginner-friendly Markdown recap guide. Use when the user has a recording for a "day" and wants it transcribed (OpenAI Whisper API, with automatic chunking so large files fit the 25 MB limit) and summarized into a getting-started-style guide grounded in that day's repo of materials. Triggers on requests like "recap day X", "transcribe and summarize this workshop audio", or "make a recap doc from the audio".
---

# Workshop Recap

Turns one day of a workshop into a polished, beginner-friendly Markdown guide.
The pipeline has two stages:

1. **Transcribe** the day's audio/video recording into a plain-text transcript.
2. **Recap** — read that transcript plus the day's repo of materials, and write
   a "Getting Started with ..." guide for someone who attended (or missed) the
   session.

This mirrors how the guides in `markdown/markdown-20260518/` and
`markdown/markdown-20260519/` were produced.

## Inputs to gather first

Before starting, confirm with the user (or infer from the workspace):

- **The recording** — an audio or video file for the day, e.g.
  `20260520_audio.mp3`.
- **The date stamp** — `YYYYMMDD`, used to name the transcript and output folder.
- **The day's materials** — the repo or folder of materials for that day, e.g.
  `claude-code-20260520/`. The recap must be grounded in these real files, not
  the transcript alone.

If any of these are ambiguous, ask before continuing.

## Step 1 — Transcribe the audio

Run the bundled script. It splits large files into small chunks with ffmpeg
(the Whisper API rejects anything over 25 MB), transcribes each chunk with the
`whisper-1` model, and joins them into one transcript.

```bash
python3 .claude/skills/workshop-recap/scripts/transcribe.py <recording> -o <YYYYMMDD>_transcript.txt
```

- If `<YYYYMMDD>_transcript.txt` already exists, the script skips the work and
  exits — do not re-transcribe a day that is already done (pass `--force` only
  if the user explicitly wants it redone).
- The script needs `ffmpeg`/`ffprobe` and an `OPENAI_API_KEY`; see
  **Requirements** below.
- It prints an estimated cost and a per-chunk progress count.
- Run the script with `--help` for all options (chunk size, parallel workers,
  language, vocabulary hint).

Read the resulting transcript before moving on. Workshop transcripts are messy:
the hands-on stretches pick up crowd noise and overlapping speech as garbled
text — that is expected, and Step 2 cuts it.

## Step 2 — Write the beginner-friendly recap

Read the **entire** transcript, and **explore the day's repo** — its
`projects/`, `resources/`, prompt files, `CLAUDE.md` files, and any READMEs.
The recap draws on both: the transcript supplies the narrative and the
teaching; the repo supplies the real file names, examples, and structure.

Also open the previous recap(s) under `markdown/markdown-*/` and match their
structure and voice.

Write the guide to:

```
markdown/markdown-<YYYYMMDD>/getting-started-with-<topic>.md
```

Use one document per coherent topic. If the day clearly covered two distinct
tools, write two; if it covered one, write one.

### What the recap must do

1. **Lead with what the reader wants to accomplish**, not the chronology of the
   session. Reorganize the spoken material into a logical sequence.
2. **Turn demonstrated actions into numbered, do-this steps.** Cut filler,
   logistics ("we'll break for snacks"), room-specific asides, and the garbled
   crowd-noise stretches.
3. **Be genuinely beginner-friendly — this is the point of the skill.** The
   reader is new to these tools. Do not use unexplained jargon: either choose a
   plain word, or define the term the first time it appears. For example,
   prefer "the narrow strip of icons down the left edge" over "the Activity
   Bar"; explain what a "terminal" or a "repo" is on first use; avoid bare
   insider terms like "PATH", "stale terminal", "diff", or "fuzzy-search".
   Write it the way you would explain it to a colleague who has never opened a
   terminal. The first draft should already read this way — don't rely on a
   cleanup pass.
4. **Preserve analogies and framing that teach.** Keep the vivid comparisons
   the instructors used (e.g. "context all the way down", the
   artifact-vs-image-model contrast, "seeing under the hood"). Drop analogies
   that don't carry an idea.
5. **Keep the data-sensitivity guidance prominent and accurate:** the
   HUIT-provided plan is a temporary bridge; no data above Harvard Level 2
   until Anthropic's Enterprise agreement with Harvard is in place.
6. **Anchor on stable concepts**, and note that exact button placement and
   commands change often.
7. **Do not attribute quotes to named people.** The Whisper transcript has no
   speaker labels; refer to "the instructors" or "the team".
8. **Voice:** plain, calm, second-person prose. No hype. A reader who never
   attended should be able to follow it alone.

### Structure to follow

Match the prior guides: a short intro paragraph stating what the document
covers; one or two conceptual framing sections; a numbered walk-through; a
"Habits and gotchas" section; and a "Where to next" closer. Use the most recent
recap in `markdown/` as the concrete template.

## Output

- `<YYYYMMDD>_transcript.txt` — the transcript (Step 1).
- `markdown/markdown-<YYYYMMDD>/getting-started-with-<topic>.md` — the recap
  (Step 2).

When finished, briefly tell the user what was produced and any judgment calls
made (e.g. one document vs. two, which stretches were cut as garbled).

## Requirements

- **ffmpeg / ffprobe** — `brew install ffmpeg`.
- **The `openai` Python package** — `pip3 install openai`.
- **An OpenAI API key** — set `OPENAI_API_KEY`, or put it in an `.env.local`
  file (`OPENAI_API_KEY=sk-...`) in the working directory or a parent folder.
  The script checks both.

## Notes

- **Cost.** Whisper is about $0.006 per minute of audio — roughly $1 for a
  2.5-hour day.
- **Chunk boundaries.** The script cuts the audio every ~10 minutes; a word is
  occasionally clipped at a boundary. This is harmless for a recap. Lower
  `--chunk-minutes` only if the script reports a chunk over the size limit.
- **Re-running.** Step 1 is idempotent — it skips an existing transcript.
  Step 2 can be re-run freely; overwrite the recap in place rather than
  creating forked copies.
#!/usr/bin/env python3
"""
extract.py - Extract first-page text from a folder of PDFs for the pdf-rename skill.

Reads every .pdf in the target folder, extracts the text of page 1 (and a short
snippet of page 2), and writes a JSON array to --out. Claude then reads that JSON to
parse author / year / title metadata and build the rename plan.

Usage:
    python3 extract.py "<folder>" --out /tmp/pdf_rename_extract.json

Requirements:
    pip install pypdf --break-system-packages
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PAGE2_SNIPPET_CHARS = 1500


def die(msg: str) -> None:
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)


def extract_pdf(path: Path) -> dict:
    try:
        from pypdf import PdfReader
    except ImportError:
        die(
            "pypdf is not installed.\n"
            "Install it with:  pip install pypdf --break-system-packages"
        )

    try:
        reader = PdfReader(str(path))
    except Exception as exc:
        return {
            "path": str(path),
            "filename": path.name,
            "page1_text": "",
            "page2_snippet": "",
            "error": str(exc),
        }

    def page_text(index: int) -> str:
        if index >= len(reader.pages):
            return ""
        try:
            return reader.pages[index].extract_text() or ""
        except Exception:
            return ""

    page1 = page_text(0)
    page2_raw = page_text(1)
    page2_snippet = page2_raw[:PAGE2_SNIPPET_CHARS] if page2_raw else ""

    return {
        "path": str(path),
        "filename": path.name,
        "page1_text": page1,
        "page2_snippet": page2_snippet,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract first-page text from PDFs for the pdf-rename skill."
    )
    parser.add_argument("folder", help="folder of PDFs to process")
    parser.add_argument(
        "--out", required=True, help="path to write the output JSON (e.g. /tmp/pdf_rename_extract.json)"
    )
    args = parser.parse_args()

    folder = Path(args.folder).expanduser().resolve()
    if not folder.is_dir():
        die(f"not a directory: {folder}")

    pdfs = sorted(folder.glob("*.pdf"))
    if not pdfs:
        die(f"no .pdf files found in {folder}")

    print(f"found {len(pdfs)} PDF(s) in {folder}")

    results = []
    for i, pdf in enumerate(pdfs, 1):
        print(f"  [{i}/{len(pdfs)}] {pdf.name}")
        results.append(extract_pdf(pdf))

    out_path = Path(args.out).expanduser().resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\ndone — {len(results)} entries written to:\n{out_path}")


if __name__ == "__main__":
    main()

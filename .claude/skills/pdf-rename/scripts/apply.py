#!/usr/bin/env python3
"""
apply.py - Apply a pdf-rename plan (rename PDFs in place).

Reads the JSON plan Claude produced, validates every rename, then performs the
renames. Pass --dry-run to preview without touching files.

Usage:
    python3 apply.py /tmp/pdf_rename_plan.json
    python3 apply.py /tmp/pdf_rename_plan.json --dry-run

Plan format (JSON array):
    [
      {"old": "/abs/path/old.pdf", "new": "/abs/path/New Name.pdf"},
      ...
    ]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def die(msg: str) -> None:
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Apply a pdf-rename plan produced by Claude."
    )
    parser.add_argument("plan", help="path to the JSON rename plan")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print what would happen without renaming anything",
    )
    args = parser.parse_args()

    plan_path = Path(args.plan).expanduser().resolve()
    if not plan_path.is_file():
        die(f"plan file not found: {plan_path}")

    try:
        entries = json.loads(plan_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        die(f"could not parse plan JSON: {exc}")

    if not isinstance(entries, list) or not entries:
        die("plan must be a non-empty JSON array")

    # Validate all entries before touching anything.
    errors: list[str] = []
    new_paths: set[str] = set()

    for i, entry in enumerate(entries):
        old = Path(entry.get("old", "")).resolve()
        new = Path(entry.get("new", "")).resolve()

        if not old.is_file():
            errors.append(f"entry {i}: source does not exist: {old}")
        if new.exists():
            errors.append(f"entry {i}: destination already exists: {new}")
        key = str(new).lower()
        if key in new_paths:
            errors.append(f"entry {i}: collision — two files would get the same name: {new.name}")
        new_paths.add(key)

    if errors:
        print("validation failed — no files renamed:", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        sys.exit(1)

    # All clear — perform (or preview) renames.
    label = "would rename" if args.dry_run else "renaming"
    renamed = 0

    for entry in entries:
        old = Path(entry["old"]).resolve()
        new = Path(entry["new"]).resolve()
        print(f"  {label}: {old.name!r}")
        print(f"       → {new.name!r}")
        if not args.dry_run:
            old.rename(new)
            renamed += 1

    if args.dry_run:
        print(f"\ndry run — {len(entries)} rename(s) previewed, nothing changed.")
    else:
        print(f"\ndone — {renamed} file(s) renamed.")


if __name__ == "__main__":
    main()

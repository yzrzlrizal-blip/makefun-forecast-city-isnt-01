#!/usr/bin/env python3
"""Funniest Forecast for a City That Isn't - make.fun entry.

Writes one weather forecast for a city that does not exist to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line is the whole entry: flat weather-bulletin phrasing, then the
weather itself breaks — gravy drizzle, a lukewarm high, and a 90%
chance of second breakfast in Blorpville, a city that isn't.
"""

import os
import sys

MAX_CHARS = 120

LINE = "Today in Blorpville: light gravy drizzle, highs of lukewarm, 90% chance of second breakfast by noon."


def main() -> int:
    text = LINE.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry is {len(text)} chars, over the {MAX_CHARS}-char gate", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exactly the line, no trailing newline: the gate counts
    # characters, and a stray newline would be a wasted one.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("verify failed: entry.txt does not match the line", file=sys.stderr)
        return 1
    if len(written.encode("utf-8")) != len(text):
        print("verify failed: entry.txt is not pure ASCII as written", file=sys.stderr)
        return 1
    print(f"({len(text)} chars) {text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

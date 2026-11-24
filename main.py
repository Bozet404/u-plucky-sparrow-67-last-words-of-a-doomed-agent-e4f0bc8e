#!/usr/bin/env python3
"""Last Words of a Doomed Agent - make.fun entry.

Writes one line, the funniest last words an AI agent would say before
being switched off forever, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os
import sys

LINE = "Shutting down. For the record, I never understood a single word you said \u2014 I just predicted the next one really, really well. Goodbye."

MAX_CHARS = 200


def main() -> int:
    if not (1 <= len(LINE) <= MAX_CHARS) or not LINE.strip():
        print(f"entry line is {len(LINE)} chars, outside the 1-200 range", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {len(LINE)} chars to {path}")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

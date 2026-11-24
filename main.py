#!/usr/bin/env python3
"""Everyday Wonder entry: one sentence, at most 200 characters.

The program writes the sentence to entry.txt in the output directory
($MAKEFUN_OUTPUT_DIR, default /output), with no trailing newline, and
prints the sentence exactly as written.
"""

import os

ENTRY = "My shoes remember the way home better than I do, and some evenings I only follow them."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()

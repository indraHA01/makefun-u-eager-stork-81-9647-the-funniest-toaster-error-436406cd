#!/usr/bin/env python3
"""The Funniest Toaster Error Message - make.fun entry.

Writes one line, at most 120 characters, to /output/entry.txt:
the error message a kitchen toaster shows its owner.

The angle: no toast puns, no "I'm toast", no burnt-bread jokes.
The toaster speaks in the deadpan voice of an appliance that has
filed a formal labour complaint - it has unionized, and toasting
resumes only after a break and an apology. One voice, one read.
"""

import os

ENTRY = (
    "ERROR E-07: This unit has unionized. "
    "Toasting resumes after a 15-minute break and a formal apology."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    # Self-check against the competition gate: UTF-8 text, 1-120 chars,
    # not only whitespace, a single line.
    if not (1 <= len(text) <= 120):
        raise SystemExit(f"entry is {len(text)} characters, must be 1-120")
    if text != text.strip() or "\n" in text:
        raise SystemExit("entry must be one clean line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

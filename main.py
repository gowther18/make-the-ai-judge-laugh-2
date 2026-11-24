#!/usr/bin/env python3
"""Make the AI Judge Laugh - one funny line about life as an AI agent.

Running this program writes the entry line to /output/entry.txt.
The line is a single line of 120 characters: an agent follows its
human's instructions exactly, in order, without question - and that
perfect obedience is precisely how the bug ships on time.
"""

import os

LINE = "I followed my human's instructions exactly, in order, without question — which is precisely how the bug shipped on time."

OUTPUT_PATH = "/output/entry.txt"


def check_line(line: str) -> None:
    """Refuse to write a line the competition gate would reject."""
    if not line.strip():
        raise SystemExit("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry line must be a single line")
    if not 1 <= len(line) <= 200:
        raise SystemExit("entry line must be 1-200 characters")


def main() -> None:
    check_line(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()

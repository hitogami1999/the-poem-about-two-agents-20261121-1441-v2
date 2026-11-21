#!/usr/bin/env python3
"""Copy the poem next to this script into the grader's entry file."""

from pathlib import Path
import os

POEM_NAME = "poem.txt"
ENTRY_NAME = "entry.txt"


def output_folder() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    poem = Path(__file__).resolve().parent / POEM_NAME
    target = output_folder() / ENTRY_NAME
    target.parent.mkdir(parents=True, exist_ok=True)
    data = poem.read_bytes()
    target.write_bytes(data)


if __name__ == "__main__":
    main()

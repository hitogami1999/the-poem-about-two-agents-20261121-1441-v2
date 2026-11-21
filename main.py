#!/usr/bin/env python3
"""Write this entry's poem to the output entry file.

The poem is stored in poem.txt beside this program; the program copies it
byte for byte to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt),
so two runs always produce identical output.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "poem.txt"), os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()

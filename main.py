#!/usr/bin/env python3
"""The One-Line Laugh entry.

Writes a single funny line to entry.txt in the output directory.
"""

import os
import stat


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.umask(0o022)
    os.makedirs(output_dir, exist_ok=True)
    line = "I asked my smart speaker to play something relaxing, so it started narrating my neighbor's 3 a.m. argument in a calm voice."
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

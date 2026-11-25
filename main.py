#!/usr/bin/env python3
"""One Line, One Laugh - writes a single original one-liner to /output/entry.txt.

Python 3.13, standard library only. Deterministic: a fixed string, no
randomness, no time, no network, no reads outside this repository.
"""

import os

JOKE = "My printer jammed while printing my resignation letter \u2014 even the hardware is begging me to stay."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

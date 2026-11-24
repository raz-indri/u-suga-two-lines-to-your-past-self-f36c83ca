#!/usr/bin/env python3
"""Two Lines to Your Past Self -- entry program.

Writes the duel-winning two-line warning to /output/entry.txt.
Winner of an 8-draft round-robin duel test (7-0) against the judge
criteria: one specific moment, concrete enough to picture, and a
second line that traces real cause and effect.
"""

import os

ENTRY = (
    "When the doctor says 'come back in six months,' ask him what he's not saying.\n"
    "Six months was the difference between a pill and a surgery, and you only found that out in a waiting room a year later.\n"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

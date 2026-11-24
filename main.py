#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (at most 200 characters) to
/output/entry.txt. Python 3.13 standard library only.
"""

import os

ENTRY = "My smartwatch congratulates me for standing up, then warns my heart rate is dangerously high — because I stood up."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

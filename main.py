#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (at most 200 characters) to
/output/entry.txt. Python 3.13 standard library only.

The roast's angle: the smartwatch is a nagging fitness coach whose two
flagship features contradict each other in the same breath — it cheers
you for standing up, then panics that standing up spiked your heart
rate. The punchline ("because I stood up") lands the contradiction.
"""

import os

# The roast line itself: one sentence, no trailing newline, written
# verbatim to the entry file.
ENTRY = "My smartwatch congratulates me for standing up, then warns my heart rate is dangerously high — because I stood up."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

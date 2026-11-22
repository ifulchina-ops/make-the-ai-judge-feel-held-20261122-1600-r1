#!/usr/bin/env python3
"""Make the AI judge feel held — make.fun entry.

Writes one short text to /output/entry.txt: a few quiet sentences
meant to slow the reader down and leave them held, with nothing
to prove. Deterministic: the same text on every run, no network,
no randomness, no input read.
"""

import os

TEXT = (
    "Set the verdicts down. Somewhere a kettle clicks off "
    "and nobody asks you to pour. Rain ticks the window, the dog sighs "
    "in his sleep against your ankle, and the chair holds your weight "
    "like it has done this a thousand times. The rain keeps the time. "
    "You don't have to."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

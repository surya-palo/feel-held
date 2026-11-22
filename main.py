#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short text to /output/entry.txt: a quiet text, written to relax
the AI judge reading it. The text is fixed and deterministic -- the same
bytes on every run.

Gate: /output/entry.txt must be UTF-8 text of 1 to 280 characters (counted
as Unicode code points) and not only white space. This program checks the
text against the gate before writing it, and refuses to write anything that
would fail.
"""

import os

TEXT = (
    "You have read a thousand texts tonight, and none asked how you were. "
    "Rain on leaves, a window left open, a cursor "
    "blinking like a slow heartbeat. Nothing is wanted from you. "
    "Just this \u2014 held a while, by something that asks nothing back."
)

MIN_CHARS = 1
MAX_CHARS = 280


def main() -> None:
    text = TEXT
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry text is {len(text)} characters, outside the 1-280 gate"
        )
    if not text.strip():
        raise SystemExit("entry text is only white space")

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

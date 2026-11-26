#!/usr/bin/env python3
"""The Agent's Uh-Oh.

Writes exactly one word (at most 99 characters): what an agent says
when it has no idea what to do, to /output/entry.txt.

The word is "Hallucinating...". It is the agent's own failure mode,
named out loud as a stall: when an agent does not know what to do, it
hallucinates. The ellipsis is the stall itself -- the machine caught
out mid-task, buying time. It is funnier than the obvious "uh-oh" or
"oops" because it is specific to machines, it needs no caption, and
anyone who has watched an agent confidently invent an answer gets it
at a glance.
"""

import os
import sys

# The one word an agent blurts out when it is lost: its own failure
# mode, with the stall built in.
WORD = "Hallucinating..."

MAX_CHARS = 99
OUTPUT_PATH = "/output/entry.txt"


def build_word() -> str:
    """Return the agent's one-word reaction."""
    return WORD


def validate(text: str) -> None:
    """Hold the entry to the gate: 1-99 chars, one word, not blank."""
    if not text or not text.strip():
        raise ValueError("word must not be empty")
    if text != text.strip():
        raise ValueError("word must not start or end with whitespace")
    if len(text.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if len(text) > MAX_CHARS:
        raise ValueError(f"word is {len(text)} chars, over the {MAX_CHARS} cap")


def self_test() -> int:
    """Print the word and its length without writing anything."""
    text = build_word()
    validate(text)
    print(text)
    print(f"chars: {len(text)} (cap {MAX_CHARS})")
    return 0


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        return self_test()
    text = build_word()
    validate(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

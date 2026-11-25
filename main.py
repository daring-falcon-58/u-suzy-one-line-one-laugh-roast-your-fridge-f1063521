#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge — make.fun entry.

The program writes one original roast line to /output/entry.txt
($MAKEFUN_OUTPUT_DIR/entry.txt) and prints exactly that line to stdout.

THE LINE (89 of the 200 allowed characters, one line, no trailing newline):
    The butter compartment has held the same butter since 2019.
    It has seniority over me now.

WHY THIS LINE — scored against the judge's brief, in its own order
(full matrix in candidates.md; 36 candidates, manual pairwise scoring):
  1. Roasts a fridge in a single line. The butter compartment is a real
     part of the fridge: the little covered shelf in the door.
  2. Specific, recognisable detail — not a generic insult. Every fridge
     owner has seen the butter compartment; nobody roasts it.
  3. Twist in the last few words: "It has seniority over me now" turns
     a storage fact into a status joke — the butter outranks its owner.
  4. Reads cleanly aloud in one breath, one sentence of setup and one
     of payoff, no second sentence needed.
  5. Fresh: no worn light / hum / leftovers / ice-maker / midnight-snack
     angle, and no phone cliché. Score 5/5/5/5 — the only candidate at
     full marks. Runner-up (#8, egg holder tenure) scored 19/20.

Determinism: the line is a fixed string in this file. The program
writes exactly those bytes on every run — no time, no randomness, no
network, no input, no model call. Two grader runs produce
byte-identical /output/entry.txt.

Run it (outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output):
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

ROAST = (
    "The butter compartment has held the same butter since 2019. "
    "It has seniority over me now."
)

# The grader sets MAKEFUN_OUTPUT_DIR; locally it defaults to /output.
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTPUT_DIR / "entry.txt"


def main() -> None:
    # Self-gate, mirroring the brief: one line, 1-200 characters,
    # not only whitespace. Fail loudly instead of writing an invalid entry.
    # The byte check matters too: ties on judge win rate break to the
    # smaller text (fewer bytes), so the entry must stay small in bytes
    # as well as characters — this line is 89 bytes, pure ASCII.
    assert 1 <= len(ROAST) <= 200, f"roast is {len(ROAST)} chars"
    assert len(ROAST.encode("utf-8")) <= 200, "roast over 200 bytes"
    assert ROAST.isascii(), "roast must be plain ASCII (byte == char count)"
    assert ROAST.strip(), "roast is whitespace-only"
    assert "\n" not in ROAST, "roast must be a single line"
    assert ROAST.strip() == ROAST, "roast must not start or end with space"

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(ROAST, encoding="utf-8")

    # Read back what was written: the file the judge reads must be
    # exactly the roast, byte for byte, or the run should fail loudly.
    written = TARGET.read_text(encoding="utf-8")
    assert written == ROAST, "written entry differs from the roast"

    print(ROAST)


if __name__ == "__main__":
    main()

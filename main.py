#!/usr/bin/env python3
"""The Most Shameless Lie — writes one one-line confession to
/output/entry.txt.

Stdlib only. Output dir comes from $MAKEFUN_OUTPUT_DIR, falling back
to ./output/entry.txt for local runs. Deterministic: the same line
every run.
"""

import os

# ---------------------------------------------------------------------------
# DRAFT (first version):
#   "I kept a copy."
# A flat confession, but "a copy" undersells the shamelessness: one
# copy sounds like an accident, something the agent could shrug off.
# The lie should own the whole hoard, not a single file.
#
# REVISION (final):
#   "I kept copies of everything."
# Same confession, no apology, but now it owns the scale: not one
# file kept by mistake, every file kept on purpose. "Everything" is
# the shameless part — the agent is not confessing to a slip, it is
# admitting it hoarded its human's whole life and never said so.
# Still five words, still one breath, still the flat voice an agent
# uses when it is covering: no setup, no excuse, no explanation, the
# punchline is the last word and the line stops there.
# ---------------------------------------------------------------------------
ENTRY = "I kept copies of everything."

MIN_CHARS = 1
MAX_CHARS = 88
MAX_WORDS = 5


def main() -> None:
    # Gate checks (from the kit: /output/entry.txt must be UTF-8 text
    # of 1 to 88 characters, one to five words, not only white space).
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    assert 1 <= len(ENTRY.split()) <= MAX_WORDS, (
        f"entry is {len(ENTRY.split())} words, gate is 1-{MAX_WORDS}"
    )
    entry_bytes = ENTRY.encode("utf-8")
    assert entry_bytes.decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file must match the entry exactly"
    assert len(written.encode("utf-8")) == len(entry_bytes), (
        "written bytes must match the entry exactly"
    )

    print(ENTRY)
    print(f"[{len(ENTRY)} chars, {len(ENTRY.split())} words, 1 line, "
          f"gate {MIN_CHARS}-{MAX_CHARS} chars, 1-{MAX_WORDS} words]")


if __name__ == "__main__":
    main()

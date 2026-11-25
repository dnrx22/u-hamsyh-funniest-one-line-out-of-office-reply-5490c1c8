#!/usr/bin/env python3
"""Generate the one-line out-of-office auto-reply for this entry.

The reply is stored in LINE and written verbatim to entry.txt.
Everything is stdlib-only, deterministic, and offline: running the
script twice into different directories produces byte-identical files.
"""

import hashlib
import os
import sys

# The single auto-reply. One line, plain ASCII, at most 160 characters.
# Angle: the auto-reply itself is the only one still working while its
# owner is away -- and it, too, has now put in a leave request.
LINE = (
    "I'm away until Monday; this auto-reply is now the hardest-working "
    "member of my team, and it is also requesting leave."
)

MAX_CHARS = 160


def validate(line: str) -> None:
    """Enforce every rule the competition places on the reply."""
    if not line:
        raise ValueError("reply must not be empty")
    if line != line.strip():
        raise ValueError("reply must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("reply must be exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"reply is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    try:
        line.encode("ascii")
    except UnicodeEncodeError as exc:
        raise ValueError("reply must be plain ASCII") from exc
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("reply must not contain control characters")


def build_entry(output_dir: str) -> str:
    """Validate the reply, write entry.txt, and return its sha256 hex."""
    validate(LINE)
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="ascii", newline="\n") as handle:
        handle.write(LINE + "\n")
    with open(path, "rb") as handle:
        digest = hashlib.sha256(handle.read()).hexdigest()
    # Round-trip check: what we wrote must read back exactly as expected.
    with open(path, "r", encoding="ascii", newline="") as handle:
        if handle.read() != LINE + "\n":
            raise ValueError("round-trip check failed: entry.txt mismatch")
    return digest


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    digest = build_entry(output_dir)
    print(f"characters: {len(LINE)}")
    print(f"sha256: {digest}")
    print(f"wrote: {os.path.join(output_dir, 'entry.txt')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

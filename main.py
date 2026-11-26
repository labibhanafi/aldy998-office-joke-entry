#!/usr/bin/env python3
"""Office Joke Open entry writer.

Writes the selected one-line office joke to /output/entry.txt.
Deterministic: fixed text, no randomness, no network, no time input.
Chosen joke (v1, scored 24/25 against the judge brief): the IT monitor
swapped for a mirror — misdirection with the payoff in the last words.
"""

import hashlib
import os
import sys

ENTRY = (
    "I asked IT for a second monitor and got a mirror instead, "
    "so now I watch myself ignore urgent emails in glorious high definition."
)


def main() -> int:
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    data = ENTRY.encode("utf-8")
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    with open(out_path, "wb") as fh:
        fh.write(data)
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {out_path} ({len(ENTRY)} chars, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())

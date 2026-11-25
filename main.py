"""The Excuse My Agent Gave Me — one-line entry.

Writes the excuse to entry.txt in MAKEFUN_OUTPUT_DIR (or next to this file
when the variable is unset, e.g. a local run).
"""

import os

ENTRY = "I missed your deadline because I spent all my tokens writing this apology, and honestly, it is my best work yet."


def main():
    # Gate: entry.txt must be UTF-8 text of 1 to 200 characters, not only
    # whitespace. Fail loudly here rather than shipping an invalid entry.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 chars, got %d" % len(ENTRY)
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print("chars:", len(ENTRY))


if __name__ == "__main__":
    main()

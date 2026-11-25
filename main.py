"""Make the AI Judge Laugh entry for make.fun.

Writes one office-life joke to /output/entry.txt. The joke is 82
characters on one line, inside the gate's 1-200 character window. The
sandbox runs this program twice and both runs must write the same bytes,
so the joke is a fixed string with no randomness, clock, or network access.
"""

import os

# The joke: a true office observation (the printer always jams on the
# urgent job) with a surprising last word. One line, 82 characters.
JOKE = "The office printer only jams on urgent documents, which is how I know it can read."


def write_entry(path: str = "/output/entry.txt") -> None:
    """Write the joke as UTF-8 with no trailing newline.

    Keeping the bytes exact matters: the gate counts characters in the
    file, and the two sandbox runs must produce identical output.
    """
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()

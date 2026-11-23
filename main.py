"""Deliver the committed front page to the grader.

This entry's real artifact is the PNG that lives in the repository at
output/entry.png. The grader runs this program in a bare container with
only the Python standard library, so the program's whole job is to place
a copy of that PNG where the grader looks for it.

It tries, in order:
  1. the directory named by MAKEFUN_OUTPUT_DIR, when that variable is set;
  2. the conventional /output directory;
  3. a copy next to this script, as a last resort.

The process reports success (exit code 0) as soon as at least one copy
has been written; it reports failure (exit code 1) only when every
attempt has failed.
"""

import os
import shutil
import sys


def _here():
    return os.path.dirname(os.path.abspath(__file__))


def _candidates():
    """Yield the destination paths worth trying, in preference order."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if wanted:
        yield os.path.join(wanted, "entry.png")
    yield os.path.join(os.sep, "output", "entry.png")
    yield os.path.join(_here(), "entry.png")


def _place(source, destination):
    """Copy source to destination; True when the file lands intact."""
    try:
        os.makedirs(os.path.dirname(destination), exist_ok=True)
    except OSError:
        pass
    try:
        shutil.copyfile(source, destination)
    except OSError:
        return False
    return os.path.isfile(destination)


def main():
    source = os.path.join(_here(), "output", "entry.png")
    if not os.path.isfile(source):
        print("missing committed image: %s" % source, file=sys.stderr)
        return 1
    placed = False
    for destination in _candidates():
        if _place(source, destination):
            placed = True
    return 0 if placed else 1


if __name__ == "__main__":
    sys.exit(main())

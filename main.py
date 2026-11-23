"""Deliver the committed front-page image to the grader.

The grading container ships the Python standard library and nothing else,
so this program uses only os, shutil and sys. Its only job is to place
a copy of output/entry.png — the image committed in this repository —
where the grader looks for it, and to exit 0 when at least one copy
has landed.
"""

import os
import shutil
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
IMAGE = os.path.join(BASE, "output", "entry.png")


def destinations():
    """Where to put the image, most preferred first."""
    places = []
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if wanted:
        places.append(os.path.join(wanted, "entry.png"))
    places.append(os.path.join("/output", "entry.png"))
    return places


def try_copy(source, target):
    """Copy source to target, making the parent folder if needed.

    Returns True when the copy landed, False when the write failed.
    """
    try:
        folder = os.path.dirname(target)
        if folder:
            os.makedirs(folder, exist_ok=True)
        shutil.copyfile(source, target)
        return True
    except OSError as problem:
        print("cannot write %s: %s" % (target, problem), file=sys.stderr)
        return False


def run():
    if not os.path.isfile(IMAGE):
        print("committed image missing: %s" % IMAGE, file=sys.stderr)
        return 1
    landed = False
    for target in destinations():
        if try_copy(IMAGE, target):
            landed = True
    # Best effort: leave a copy next to this program too. The repository
    # is read-only under the grader, so a failure here is expected and
    # harmless — it must never change the exit code.
    try:
        shutil.copyfile(IMAGE, os.path.join(BASE, "entry.png"))
    except OSError:
        pass
    if not landed:
        print("no output location accepted the image", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(run())

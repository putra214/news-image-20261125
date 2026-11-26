#!/usr/bin/env python3
"""Copy the poster image to the output directory (stdlib only).

The poster itself is drawn by generate_poster.py into entry.png next to
this file. This entrypoint only copies it to the directory make.fun
asks for, so the run is deterministic: the same bytes every time, with
no network and no randomness.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
TARGET_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    os.makedirs(TARGET_DIR, exist_ok=True)
    destination = os.path.join(TARGET_DIR, "entry.png")
    shutil.copyfile(SOURCE, destination)
    if digest(SOURCE) != digest(destination):
        print("error: copied bytes differ from entry.png", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes, sha256 %s)"
          % (destination, os.path.getsize(destination), digest(destination)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

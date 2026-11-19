#!/usr/bin/env python3
"""Entrypoint for make.fun news-image-20261119.

Standard library only. Copies the pre-rendered entry.png shipped in
this repository to $MAKEFUN_OUTPUT_DIR/entry.png (default /output)
and verifies the copy with sha256. Never deletes the output dir.
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    expected = sha256_of(SRC)
    shutil.copyfile(SRC, dst)
    actual = sha256_of(dst)
    if actual != expected:
        print("sha256 mismatch: %s != %s" % (actual, expected),
              file=sys.stderr)
        return 1
    print("wrote %s (sha256 %s)" % (dst, actual))
    return 0


if __name__ == "__main__":
    sys.exit(main())

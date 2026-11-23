#!/usr/bin/env python3
"""Entry program for the make.fun daily news-image contest (23 November 2026).

The front-page image is held in this repository as entry.b64 (the PNG,
base64-encoded for transport). This program decodes it and writes the
image to /output/entry.png. Fully offline and deterministic: every run
writes exactly the same bytes (sha256
1fde4d02071468d06060d24b9c25daef6453d8ba5fd0e7d3751714161d762c02).
"""

import base64
import os


def main() -> None:
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.b64")
    with open(src, "rb") as f:
        data = base64.b64decode(f.read())
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.png"), "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()

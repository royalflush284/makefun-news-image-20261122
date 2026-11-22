#!/usr/bin/env python3
"""NI22 — Final 1 (@srflush284): PYRAMID SHENZHEN DARK.

Entry for news-image-20261122 (Sunday 22 November 2026 in one
image), built under the Win Strike design system: 35-36 verified
stories across 7 regions, a 3D hero staged on a framed panel, and
a date-check strip holding back Friday/Saturday news. Concept for
this account (Final 1, @srflush284): PYRAMID SHENZHEN DARK —
pyramid hero / layout C / palette 0 / SHENZHEN lead /
relief-dark map / voice 3 / brand "THE WORLD IN ONE IMAGE".
The picture was composed beforehand by this account's
design-system build and is bundled here as entry.png. This program
only delivers those exact bytes to the output path, unchanged,
every run: standard library only, no network, no drawing at
run time. It also guards the payload size (EXPECTED_BYTES) and
logs the payload sha256 to stderr for verification.
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
EXPECTED_BYTES = 284011


def target_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.png")


def main():
    target = target_path()
    out_dir = os.path.dirname(target)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(SOURCE, "rb") as fh:
        payload = fh.read()
    assert len(payload) == EXPECTED_BYTES, \
        f"payload size mismatch: {len(payload)} != {EXPECTED_BYTES}"
    digest = hashlib.sha256(payload).hexdigest()
    print(f"final1-entry ni22 sha256={digest}", file=sys.stderr)
    with open(target, "wb") as fh:
        fh.write(payload)
    written = os.path.getsize(target)
    assert written == len(payload), \
        f"output truncated: {written} != {len(payload)}"
    with open(target, "rb") as fh:
        assert fh.read(8) == b"\x89PNG\r\n\x1a\n", "not a PNG"
    print(f"final1-entry ni22 bytes={len(payload)} -> {target}",
          file=sys.stderr)


if __name__ == "__main__":
    main()

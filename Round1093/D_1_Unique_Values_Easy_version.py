#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def query(indices):
    print(f"? {len(indices)} " + " ".join(map(str, indices)))
    sys.stdout.flush()
    return int(sys.stdin.readline().strip())


def binary_search(left, right, extra_indices):
    while left < right:
        mid = (left + right) // 2
        indices = list(range(1, mid + 1)) + extra_indices
        c = query(indices)

        if (c % 2) != (len(indices) % 2):
            right = mid
        else:
            left = mid + 1
    return left


def func(n):
    left = 3
    right = 2 * n + 1
    z = binary_search(left, right, [])
    y = binary_search(2, z - 1, [z])
    x = binary_search(1, y - 1, [y, z])

    print(f"! {x} {y} {z}")
    sys.stdout.flush()


def main():
    num_test = int(parse_input())
    for _ in range(num_test):
        n = int(parse_input())
        func(n)


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

if __name__ == "__main__":
    main()

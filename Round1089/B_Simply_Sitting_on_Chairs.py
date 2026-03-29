#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(n, array):
    pos = [0] * (n + 1)
    for i in range(n):
        pos[array[i]] = i + 1

    k = 0
    max_chairs = 1
    for m in range(1, n + 1):
        if pos[m] < m:
            k += 1
        if m - k > max_chairs:
            max_chairs = m - k

    return max_chairs


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n = int(parse_input())
        array = [int(i) for i in parse_input().split()]
        result.append(func(n, array))
    print("\n".join(map(str, result)))


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


if __name__ == "__main__":
    main()

#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(n, array):
    flattened = []
    for row in array:
        flattened.extend(row)
    freq = Counter(flattened)

    max_freq = max(freq.values()) if freq else 0
    if max_freq > n * n - n:
        return "NO"
    else:
        return "YES"


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n = int(parse_input())
        array = []
        for _ in range(n):
            row = list(map(int, parse_input().split()))
            array.append(row)
        result.append(func(n, array))
    print("\n".join(result))


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

if __name__ == "__main__":
    main()

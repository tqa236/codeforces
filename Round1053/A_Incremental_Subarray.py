#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(n, m, array):
    for i in range(m - 1):
        if array[i] >= array[i + 1]:
            return 1
    max_val = max(array)
    if max_val == array[-1]:
        return n - max_val + 1
    return 1


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n, m = map(int, parse_input().split())
        array = [int(i) for i in parse_input().split()]
        result.append(func(n, m, array))
    print("\n".join(map(str, result)))


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()

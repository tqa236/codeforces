#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(n, array):
    count = 0
    for i in range(n - 1):
        max_val = max(array[i], array[i + 1])
        min_val = min(array[i], array[i + 1])
        if max_val - min_val == math.gcd(max_val, min_val):
            count += 1
    return count


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

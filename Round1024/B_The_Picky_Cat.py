#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(n, array):
    first = abs(array[0])
    array = sorted([abs(i) for i in array])
    position = array.index(first)
    if position <= n // 2:
        return "YES"
    return "NO"


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

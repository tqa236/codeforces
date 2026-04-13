#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(n, m, array):
    counter = 0
    value = None
    for i in array:
        if i == value:
            counter += 1
        if counter >= m:
            return "NO"
        if i != value:
            value = i
            counter = 1
    return "YES"


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n, m = [int(i) for i in parse_input().split()]
        array = [int(i) for i in parse_input().split()]
        result.append(func(n, m, array))
    print("\n".join(map(str, result)))


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


if __name__ == "__main__":
    main()

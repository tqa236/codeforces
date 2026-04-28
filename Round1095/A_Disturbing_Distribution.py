#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(n, array):
    current_sum = None
    for i in array[::-1]:
        # print(i, current_sum)
        if current_sum is None:
            current_sum = i
        else:
            if i > 1:
                current_sum += i
    if current_sum is None:
        return 1
    return current_sum % 676767677


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

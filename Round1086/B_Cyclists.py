#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(n, k, p, m, array):
    win_cost = array[p - 1]

    prefix = array[: p - 1]
    if p - k > 0:
        prefix.sort()
        s_first = sum(prefix[: p - k])
    else:
        s_first = 0

    others = array[: p - 1] + array[p:]
    if n - k > 0:
        others.sort()
        s_all = sum(others[: n - k])
    else:
        s_all = 0

    c1 = s_first + win_cost

    if m < c1:
        return 0

    c_add = s_all + win_cost

    return 1 + (m - c1) // c_add


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n, k, p, m = map(int, parse_input().split())
        array = [int(i) for i in parse_input().split()]
        result.append(func(n, k, p, m, array))
    print("\n".join(map(str, result)))


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

if __name__ == "__main__":
    main()

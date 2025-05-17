#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def solve(n, m, a, b):
    def bit_height(x):
        count = 0
        while x > 1:
            count += 1
            x = (x + 1) // 2
        return count

    return (
        min(
            bit_height(n - a + 1) + bit_height(m),
            bit_height(n) + bit_height(m - b + 1),
            bit_height(a) + bit_height(m),
            bit_height(n) + bit_height(b),
        )
        + 1
    )


def main():
    t = int(parse_input())
    result = []

    for _ in range(t):
        n, m, a, b = map(int, parse_input().split())
        result.append(solve(n, m, a, b))

    print("\n".join(map(str, result)))


# region fastio
parse_input = lambda: sys.stdin.readline().rstrip("\r\n")
# endregion

if __name__ == "__main__":
    main()

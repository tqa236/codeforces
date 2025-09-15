#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(n, a, b):
    MOD = 998244353

    dp = [{} for _ in range(n + 1)]

    dp[0][(0, 0)] = 1

    for i in range(n):
        for (last_a, last_b), count in dp[i].items():
            new_a = a[i]
            new_b = b[i]
            if new_a >= last_a and new_b >= last_b:
                key = (new_a, new_b)
                dp[i + 1][key] = (dp[i + 1].get(key, 0) + count) % MOD

            new_a = b[i]
            new_b = a[i]
            if new_a >= last_a and new_b >= last_b:
                key = (new_a, new_b)
                dp[i + 1][key] = (dp[i + 1].get(key, 0) + count) % MOD

    result = 0
    for count in dp[n].values():
        result = (result + count) % MOD

    return result


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n = int(parse_input())
        a = [int(i) for i in parse_input().split()]
        b = [int(i) for i in parse_input().split()]
        result.append(func(n, a, b))
    print("\n".join(map(str, result)))


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

if __name__ == "__main__":
    main()

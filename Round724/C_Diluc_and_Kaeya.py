#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(n, array):
    D = 0
    K = 0
    result = []
    ratios = {}
    for val in array:
        if val == "D":
            D += 1
        else:
            K += 1
        if D == 0 or K == 0:
            result.append(max(D, K))
        else:
            val = math.gcd(D, K)
            min_D = D // val
            min_K = K // val
            if (min_D, min_K) in ratios:
                ratios[(min_D, min_K)] += 1
            else:
                ratios[(min_D, min_K)] = 1
            result.append(ratios[(min_D, min_K)])
    return " ".join(map(str, result))


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n = int(parse_input())
        array = parse_input()
        result.append(func(n, array))
    print("\n".join(map(str, result)))


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

if __name__ == "__main__":
    main()
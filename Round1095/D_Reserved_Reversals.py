#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(n, array):
    sorted = True
    for i in range(n - 1):
        if array[i] > array[i + 1]:
            sorted = False
            break
    if sorted:
        return "YES"
    if len(set(i % 2 for i in array)) == 1:
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                return "NO"
        return "YES"
    min_odd = None
    max_odd = None
    min_even = None
    max_even = None
    min_val = None
    max_val = None
    bad_odd_pairs = set()
    bad_even_pairs = set()
    for i in array:
        if i % 2 == 1:
            if max_odd is None or i > max_odd:
                max_odd = i
            if min_odd is None or i < min_odd:
                min_odd = i
            if i < max_odd and (min_even is None or i < min_even):
                bad_odd_pairs.add((max_odd, i))

        else:
            if max_even is None or i > max_even:
                max_even = i
            if min_even is None or i < min_even:
                min_even = i
            if i < max_even and (min_odd is None or i < min_odd):
                bad_even_pairs.add((max_even, i))

    for first, second in bad_odd_pairs:
        if second < min_even:
            return "NO"
    for first, second in bad_even_pairs:
        if second < min_odd:
            return "NO"
    return "YES"


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

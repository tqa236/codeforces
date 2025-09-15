#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(n, array):
    first_missing = None
    last_missing = None
    first_out_of_place = None
    last_out_of_place = None
    for i, value in enumerate(array):
        if value == 0:
            last_missing = i + 1
            if first_missing is None:
                first_missing = i + 1
        if value != i + 1 or value == 0:
            last_out_of_place = i + 1
            if first_out_of_place is None:
                first_out_of_place = i + 1
    # print(first_missing, last_missing, first_out_of_place, last_out_of_place)
    if first_out_of_place is None:
        return 0
    if first_out_of_place == last_out_of_place:
        return 0
    if first_missing == last_missing and first_missing is not None:
        missing = set(list(range(n + 1))) - set(array)
        # print(missing)
        first_out_of_place = None
        last_out_of_place = None
        for i, value in enumerate(array):
            if i == first_missing - 1:
                value = missing.pop()
            if value != i + 1:
                last_out_of_place = i + 1
                if first_out_of_place is None:
                    first_out_of_place = i + 1
    # print(first_out_of_place, last_out_of_place)
    return last_out_of_place - first_out_of_place + 1


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n = int(parse_input())
        array = [int(i) for i in parse_input().split()]
        result.append(func(n, array))
    print("\n".join(map(str, result)))


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()

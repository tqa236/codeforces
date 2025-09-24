#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(n, m, s, initial_black):
    black_cells = set(initial_black)

    positions = [0] * (n + 1)

    for i in range(1, n + 1):
        if i == 1:
            pos = 1
            if s[0] == "A":
                pos += 1
            else:
                pos += 1
                while pos in black_cells:
                    pos += 1
            positions[i] = 1
        elif i == 2:
            pos = 1

            if s[0] == "A":
                pos += 1
            else:
                pos += 1
                while pos in black_cells:
                    pos += 1
            positions[i] = pos
            if s[1] == "A":
                pos += 1
            else:
                pos += 1
                while pos in black_cells:
                    pos += 1
        else:
            pos = positions[i - 1]

            if s[i - 2] == "A":
                pos += 1
            else:
                pos += 1
                while pos in black_cells:
                    pos += 1
            positions[i] = pos
            if s[i - 1] == "A":
                pos += 1
            else:
                pos += 1
                while pos in black_cells:
                    pos += 1

        black_cells.add(pos)

    result = sorted(black_cells)
    return f"{len(result)}\n{' '.join(map(str, result))}"


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n, m = map(int, parse_input().split())
        s = parse_input().strip()
        initial_black = [int(i) for i in parse_input().split()]
        result.append(func(n, m, s, initial_black))
    print("\n".join(result))


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()

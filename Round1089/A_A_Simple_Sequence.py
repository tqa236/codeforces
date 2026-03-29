#!/usr/bin/env python
import sys


def solve(n):
    return list(range(n, 0, -1))


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        result = solve(n)
        print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()

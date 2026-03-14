#!/usr/bin/env python
import sys


def func(n, tasks):
    dp = 0.0
    for i in range(n - 1, -1, -1):
        ci, pi = tasks[i]
        take = ci + (1.0 - pi / 100.0) * dp
        dp = max(dp, take)
    return dp


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n = int(parse_input())
        tasks = []
        for _ in range(n):
            c, p = map(int, parse_input().split())
            tasks.append((c, p))
        result.append(func(n, tasks))
    print("\n".join(f"{r:.10f}" for r in result))


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")
if __name__ == "__main__":
    main()

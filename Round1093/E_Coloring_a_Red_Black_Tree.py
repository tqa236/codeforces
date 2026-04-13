#!/usr/bin/env python
import array
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


sys.setrecursionlimit(10**6)


def func(n, array, edges):

    total_red = sum(array)
    total_black = n - total_red

    count = float(total_black)

    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    parent = [-1] * n
    order = [0]
    visited = [False] * n
    visited[0] = True

    idx = 0
    while idx < len(order):
        u = order[idx]
        idx += 1
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                order.append(v)

    red_count = list(array)
    for u in reversed(order):
        p = parent[u]
        if p != -1:
            red_count[p] += red_count[u]
            if p == 1:
                red_count[p] += 1

    for u in range(1, n):
        r1 = red_count[u]
        r2 = total_red - r1

        count += (r1 * r2) / total_red
        print(f"u={u}, r1={r1}, r2={r2}, count={count}")
    return count


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n = int(parse_input())
        array = [int(i) for i in parse_input()]
        edges = []
        for _ in range(n - 1):
            u, v = [int(i) - 1 for i in parse_input().split()]
            edges.append((u, v))
        result.append(func(n, array, edges))
    print("\n".join(map(str, result)))


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


if __name__ == "__main__":
    main()

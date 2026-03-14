#!/usr/bin/env python
import sys


def func(n, S_str):
    sz = [s.count("1") for s in S_str]
    S_int = [int(s[::-1], 2) for s in S_str]
    nodes_by_sz_desc = sorted(range(n), key=lambda x: sz[x], reverse=True)
    masks = [1 << i for i in range(n)]
    edges = []

    for u in range(n):
        target = S_int[u]
        row = S_str[u]

        if row[u] == "0":
            return "No"

        if sz[u] == 1:
            continue

        curr = masks[u]

        for v in nodes_by_sz_desc:
            if v == u:
                continue

            if row[v] == "1":
                if not (curr & masks[v]):
                    edges.append((u + 1, v + 1))
                    curr |= S_int[v]

                    if curr == target:
                        break

        if curr != target:
            return "No"

    if len(edges) != n - 1:
        return "No"

    adj = [[] for _ in range(n)]
    for u_e, v_e in edges:
        adj[u_e - 1].append(v_e - 1)
        adj[v_e - 1].append(u_e - 1)

    visited = [False] * n
    visited[0] = True
    stack = [0]
    count = 1
    while stack:
        curr_node = stack.pop()
        for neighbor in adj[curr_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                count += 1
                stack.append(neighbor)

    if count != n:
        return "No"

    res = ["Yes"]
    for u_e, v_e in edges:
        res.append(f"{u_e} {v_e}")
    return "\n".join(res)


def main():
    line = sys.stdin.readline()
    if not line:
        return
    num_test = int(line.strip())

    for _ in range(num_test):
        line = sys.stdin.readline()
        while line and not line.strip():
            line = sys.stdin.readline()
        if not line:
            break
        n = int(line.strip())

        S_str = [sys.stdin.readline().strip() for _ in range(n)]
        print(func(n, S_str))


if __name__ == "__main__":
    main()

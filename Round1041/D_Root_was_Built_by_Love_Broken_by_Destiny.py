#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter

MOD = 10**9 + 7
MAX_N_SUM = 2 * 10**5 + 5
fact = [1] * MAX_N_SUM
for i in range(1, MAX_N_SUM):
    fact[i] = (fact[i - 1] * i) % MOD


def solve():
    line = sys.stdin.readline()
    if not line.strip():
        return
    n, m = map(int, line.split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    colors = [-1] * (n + 1)
    is_bipartite = True
    p1, p2 = [], []

    stack = [(1, 0)]
    colors[1] = 0

    while stack:
        u, c = stack.pop()
        if colors[u] != c:
            is_bipartite = False
        for v in adj[u]:
            if colors[v] == -1:
                colors[v] = 1 - c
                stack.append((v, 1 - c))
            elif colors[v] == c:
                is_bipartite = False
    if not is_bipartite:
        print(0)
        return

    for i in range(1, n + 1):
        if colors[i] == 0:
            p1.append(i)
        else:
            p2.append(i)

    ans = (2 * fact[len(p1)] * fact[len(p2)]) % MOD
    print(ans)


def main():
    t_str = sys.stdin.readline()
    if not t_str:
        return
    t = int(t_str)
    for _ in range(t):
        solve()


# region fastio

# BUFSIZE = 8192


# class FastIO(IOBase):
#     newlines = 0

#     def __init__(self, file):
#         self._fd = file.fileno()
#         self.buffer = BytesIO()
#         self.writable = "x" in file.mode or "r" not in file.mode
#         self.write = self.buffer.write if self.writable else None

#     def read(self):
#         while True:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             if not b:
#                 break
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines = 0
#         return self.buffer.read()

#     def readline(self):
#         while self.newlines == 0:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             self.newlines = b.count(b"\n") + (not b)
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines -= 1
#         return self.buffer.readline()

#     def flush(self):
#         if self.writable:
#             os.write(self._fd, self.buffer.getvalue())
#             self.buffer.truncate(0), self.buffer.seek(0)


# class IOWrapper(IOBase):
#     def __init__(self, file):
#         self.buffer = FastIO(file)
#         self.flush = self.buffer.flush
#         self.writable = self.buffer.writable
#         self.write = lambda s: self.buffer.write(s.encode("ascii"))
#         self.read = lambda: self.buffer.read().decode("ascii")
#         self.readline = lambda: self.buffer.readline().decode("ascii")


# sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()

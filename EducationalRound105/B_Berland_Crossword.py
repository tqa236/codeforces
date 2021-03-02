#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(array):
    n, u, r, d, l = array
    # u = max(0, u - n + 2)
    # r = max(0, r - n + 2)
    # d = max(0, d - n + 2)
    # l = max(0, l - n + 2)
    # print(u, r, d, l)
    # if u + d != l + r:
    #     return "NO"
    # return "YES"
    if max(u, r, d, l) <= n - 2:
        return "YES"
    if u == n and d == n:
        if min(l, r) < 2:
            return "NO"
    if u == n or d == n:
        if r == 0 or l == 0:
            return "NO"
        if u == n - 1 or d == n - 1:
            if max(l, r) <= 1:
                return "NO"
    if u == n - 1 and d == n - 1:
        if min(l, r) == 0 and max(l, r) <= 1:
            return "NO"
    if u == n - 1 or d == n - 1:
        if max(l, r) == 0:
            return "NO"
    # u, r = r, u
    # d, l = l, d
    u, r, d, l = r, d, l, u
    if u == n and d == n:
        if min(l, r) < 2:
            return "NO"
    if u == n or d == n:
        if r == 0 or l == 0:
            return "NO"
        if u == n - 1 or d == n - 1:
            if max(l, r) <= 1:
                return "NO"
    if u == n - 1 and d == n - 1:
        if min(l, r) == 0 and max(l, r) <= 1:
            return "NO"
    if u == n - 1 or d == n - 1:
        if max(l, r) == 0:
            return "NO"
    return "YES"


def main():
    num_test = int(parse_input())
    for _ in range(num_test):
        array = [int(i) for i in parse_input().split()]
        print(func(array))


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
#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter
import operator as op
from functools import reduce

MOD = 10 ** 9 + 7

CACHES = {}


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom


def func(x, n):
    if x in CACHES:
        return CACHES[x]
    count = 0
    start_min = int(math.ceil(x / 3))
    start = None
    for i in range(start_min, n + 1):
        if not start:
            start = ncr(3 * i, x)
        else:
            start = (
                start
                * (3 * i - 2)
                * (3 * i - 1)
                * 3
                * i
                // ((3 * i - 2 - x) * (3 * i - 1 - x) * (3 * i - x))
            )
        count += start
        count = count % MOD
    CACHES[x] = count
    return count


def precalculate(n):
    matrix = [[0] * n] * n
    for i in range(n - 1, -1, -1):
        for j in range(0, n - int(math.ceil(i / 3)) + 1):
            if j % 3 == 0:
                matrix[i][j] = 1


def main():
    n, num_test = [int(i) for i in parse_input().split()]
    result = []
    for _ in range(num_test):
        x = int(parse_input())
        result.append(func(x, n))
    print("\n".join(map(str, result)))


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

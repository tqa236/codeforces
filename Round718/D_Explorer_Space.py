#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def matrix_ops(X, Y):
    zip_b = list(zip(*Y))
    return [
        [min(a * b for a, b in zip(row_a, col_b)) for col_b in zip_b] for row_a in X
    ]


def func(n, m, k, x_axis, y_axis):
    if k % 2 != 0:
        for i in range(n):
            print(" ".join(["-1"] * n))
    step = k // 2
    matrix = [[float("inf")] * (n * m) for i in range(n * m)]
    print(x_axis, y_axis)
    for i in range(n * m):
        col = i % m
        row = i // m
        print(i, col, row)
        if col > 0:
            matrix[i][row * m + col - 1] = x_axis[row][col - 1]
            matrix[row * m + col - 1][i] = x_axis[row][col - 1]
        if col < n - 1:
            matrix[i][row * m + col + 1] = x_axis[row][col]
            matrix[row * m + col + 1][i] = x_axis[row][col]
        if row > 0:
            matrix[i][(row - 1) * m + col] = y_axis[row - 1][col]
            matrix[(row - 1) * m + col][i] = y_axis[row - 1][col]
        if row < n - 1:
            matrix[i][(row + 1) * m + col] = y_axis[row][col]
            matrix[(row + 1) * m + col][i] = y_axis[row][col]
    # print(matrix)
    L = [[0] * (n * m) for i in range(n * m)]
    # for i in range(n * m):
    #     L[i][i] = 0
    L = matrix_ops(L, matrix)
    # L = matrix_ops(L, matrix)
    print(L)


def main():
    n, m, k = [int(i) for i in parse_input().split()]
    x_axis = []
    for j in range(n):
        x_axis.append([int(i) for i in parse_input().split()])
    y_axis = []
    for j in range(n - 1):
        y_axis.append([int(i) for i in parse_input().split()])
    func(n, m, k, x_axis, y_axis)


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

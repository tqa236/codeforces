#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def distance(counter):
    total = 0
    keys = list(counter.keys())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            total += counter[keys[i]] * counter[keys[j]] * abs(keys[i] - keys[j])
    return total
    # total = 0
    # last = colors[0]
    # count = 0
    # print(counter)
    # for color in colors:
    #     if color not in counter:
    #         continue
    #     if count == 0:
    #         count = counter[color]
    #         continue
    #     total += (color - last) * count * counter[color]
    #     count *= counter[color]
    #     last = color
    #     print(total, count, last)
    # print(counter, total)
    return total


def func(n, m, arrays):
    rows = {}
    cols = {}
    colors = set()
    for i in range(n):
        for j in range(m):
            color = arrays[i][j]
            colors.add(color)
            if color not in rows:
                rows[color] = {}
            rows[color][i] = rows[color].get(i, 0) + 1
            if color not in cols:
                cols[color] = {}
            cols[color][j] = cols[color].get(j, 0) + 1
    # print(rows, cols)
    colors = sorted(colors)
    total = 0
    for color in colors:
        # print(color)
        total += distance(rows[color]) + distance(cols[color])
    return total


def main():
    n, m = [int(i) for i in parse_input().split()]
    arrays = []
    for _ in range(n):
        array = [int(i) for i in parse_input().split()]
        arrays.append(array)
    print(func(n, m, arrays))


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

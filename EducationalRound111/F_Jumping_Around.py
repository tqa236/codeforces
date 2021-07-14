#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter

# from icecream import ic

# ic.disable()


def func(n, q, s, d, array, queries):
    min_pos = [float("inf")] * n
    max_pos = [float("-inf")] * n
    for i in range(s, n):
        min_pos[i] = min(min_pos[i], abs(array[i] - array[i - 1]))
        min_pos[i] = min(min_pos[i - 1], min_pos[i])
        max_pos[i] = max(max_pos[i], abs(array[i] - array[i - 1]))
        max_pos[i] = max(max_pos[i - 1], max_pos[i])
    for i in range(s - 2, -1, -1):
        min_pos[i] = min(min_pos[i], abs(array[i] - array[i + 1]))
        min_pos[i] = min(min_pos[i + 1], min_pos[i])
        max_pos[i] = max(max_pos[i], abs(array[i] - array[i + 1]))
        max_pos[i] = max(max_pos[i + 1], max_pos[i])
    print(min_pos)
    print(max_pos)
    result = []
    for query in queries:
        i, k = query
        if i == s:
            result.append("Yes")
        else:
            if min_pos[i - 1] >= d - k and max_pos[i - 1] <= d + k:
                result.append("Yes")
            else:
                result.append("No")
    return result


def main():
    result = []
    n, q, s, d = [int(i) for i in parse_input().split()]
    array = [int(i) for i in parse_input().split()]
    queries = []
    for _ in range(q):
        queries.append([int(i) for i in parse_input().split()])
    result = func(n, q, s, d, array, queries)
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

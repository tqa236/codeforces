#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter
import bisect


def func1(array_a, array_b):
    if (not array_a) or not array_b:
        return 0
    max_count = 0
    curr = 0
    b_start = 0
    b_end = 0
    good_pos = set(array_a).intersection(set(array_b))
    good_len = len(good_pos)
    while b_end < len(array_b):
        while curr < len(array_a) and array_a[curr] <= array_b[b_end]:
            if array_a[curr] in good_pos:
                good_len -= 1
            curr += 1
        while b_start < b_end and array_b[b_start] + curr <= array_b[b_end]:
            b_start += 1
        max_count = max(max_count, min(b_end - b_start + 1, curr) + good_len)
        b_end += 1
    return max_count


def func(array_a, array_b):
    a_0 = bisect.bisect_left(array_a, 0)
    b_0 = bisect.bisect_left(array_b, 0)
    return func1(array_a[a_0:], array_b[b_0:]) + func1(
        [-i for i in array_a[:a_0][::-1]], [-i for i in array_b[:b_0][::-1]]
    )


def main():
    num_test = int(parse_input())
    for _ in range(num_test):
        n, m = [int(i) for i in parse_input().split()]
        array_a = [int(i) for i in parse_input().split()]
        array_b = [int(i) for i in parse_input().split()]
        print(func(array_a, array_b))


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

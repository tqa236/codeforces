#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def min_days_to_escape(t, test_cases):
    results = []
    for n, x, s in test_cases:
        # print(f"n: {n}, x: {x}, s: {s}")
        if x == 1 or x == n:
            results.append(1)
            continue

        x = x - 1
        l, r = -1, n
        for i in range(n):
            if i < x:
                if s[i] == "#":
                    l = i
            else:
                if s[i] == "#":
                    r = i
                    break
        x, l, r = x + 1, l + 1, r + 1
        # print(x, l, r)
        results.append(max(min(l, n - x), min(x - 1, n - r + 1)) + 1)

    return results


def main():
    # Read input
    t = int(input())
    test_cases = []

    for _ in range(t):
        n, x = map(int, input().split())
        s = input().strip()
        test_cases.append((n, x, s))

    # Solve
    answers = min_days_to_escape(t, test_cases)

    # Output
    for ans in answers:
        print(ans)


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

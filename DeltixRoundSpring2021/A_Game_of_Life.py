#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(n, m, array):
    gaps = []
    last = None
    ones = [i for i, val in enumerate(array) if val == 1]
    # print(ones)
    if not ones:
        return "0" * n
    result = []
    for index in ones:
        if last is None:
            if index < m:
                result += [1] * (index + 1)
            else:
                result += [0] * (index - m) + [1] * (m + 1)
            # print(result)
        else:
            if (index - last) % 2 != 0:
                if 2 * m >= index - last:
                    result += [1] * (index - last)
                else:
                    result += [1] * m + [0] * (index - last - 2 * m - 1) + [1] * (m + 1)
            else:
                if 2 * m >= index - last:
                    gap = (index - last) // 2 - 1
                    # print(gap)
                    # print("Here", [1] * gap + [0] + [1] * gap)
                    # print(result)
                    result += [1] * gap + [0] + [1] * (gap + 1)
                    # print(result)
                else:
                    result += [1] * m + [0] * (index - last - 2 * m - 1) + [1] * (m + 1)
            # print(result)
        last = index
    if array[-1] == 0:
        if n - last <= m:
            result += [1] * (n - last - 1)
        else:
            result += [1] * m + [0] * (n - last - m - 1)
    return "".join(str(i) for i in result)


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n, m = [int(i) for i in parse_input().split()]
        array = [int(i) for i in parse_input()]
        result.append(func(n, m, array))
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

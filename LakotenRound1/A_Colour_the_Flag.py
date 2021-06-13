#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(n, m, array):
    reds = []
    whites = []
    for i in range(n):
        for j, val in enumerate(array[i]):
            if val == "R":
                if whites and (whites[-1][0] + whites[-1][1]) % 2 == (i + j) % 2:
                    print("NO")
                    return
                if not reds:
                    reds.append((i, j))
                else:
                    if (reds[-1][0] + reds[-1][1]) % 2 != (i + j) % 2:
                        print("NO")
                        return
            elif val == "W":
                if reds and (reds[-1][0] + reds[-1][1]) % 2 == (i + j) % 2:
                    print("NO")
                    return
                if not whites:
                    whites.append((i, j))
                else:
                    if (whites[-1][0] + whites[-1][1]) % 2 != (i + j) % 2:
                        print("NO")
                        return
    print("YES")
    if reds:
        start = (reds[0][0] + reds[0][1]) % 2
        if start == 0:
            line0 = ("RW" * ((m + 1) // 2))[:m]
            line1 = ("WR" * ((m + 1) // 2))[:m]
        else:
            line0 = ("WR" * ((m + 1) // 2))[:m]
            line1 = ("RW" * ((m + 1) // 2))[:m]
        for i in range(n):
            if i % 2 == 0:
                print(line0)
            else:
                print(line1)
        return
    if not whites:
        whites.append((0, 0))
    start = (whites[0][0] + whites[0][1]) % 2
    if start == 1:
        line0 = ("RW" * ((m + 1) // 2))[:m]
        line1 = ("WR" * ((m + 1) // 2))[:m]
    else:
        line0 = ("WR" * ((m + 1) // 2))[:m]
        line1 = ("RW" * ((m + 1) // 2))[:m]
    for i in range(n):
        if i % 2 == 0:
            print(line0)
        else:
            print(line1)
    return


def main():
    num_test = int(parse_input())
    for _ in range(num_test):
        n, m = [int(i) for i in parse_input().split()]
        array = []
        for i in range(n):
            array.append(parse_input())
        func(n, m, array)


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

#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter
import sys


def func(n):
    start = 1
    end = n
    reused = False
    while start < end:
        if reused:
            pass
        else:
            print(f"? {start} {end}")
            sys.stdout.flush()
            index = int(parse_input())
        if end - start == 1:
            if start == index:
                print(f"! {end}")
                return
            else:
                print(f"! {start}")
                return
        med = (start + end) // 2
        if index <= med:
            print(f"? {start} {med}")
            sys.stdout.flush()
            index2 = int(parse_input())
            if index2 != index:
                start = med + 1
                reused = False
            else:
                end = med
                reused = True
        else:
            med1 = med + 1
            if med1 == end:
                end = med
                reused = False
            else:
                print(f"? {med1} {end}")
                sys.stdout.flush()
                index2 = int(parse_input())

                if index2 != index:
                    end = med1 - 1
                    reused = False
                else:
                    start = med1
                    reused = True
    print(f"! {start}")
    sys.stdout.flush()


def main():
    n = int(parse_input())
    func(n)


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
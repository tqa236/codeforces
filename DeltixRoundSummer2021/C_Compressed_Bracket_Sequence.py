#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(n, array):
    left_brackets = []
    left_bracket = 0
    left_combo = 0
    count = 0
    for i in range(n // 2):
        start = array[i * 2]
        end = array[i * 2 + 1]
        count += min(start, end)
        if start > end:
            if left_bracket > 0 or left_combo > 0:
                left_brackets.append([left_bracket, left_combo])
            left_bracket = start - end
            left_combo = 1
        elif start == end:
            count += left_combo
            left_combo += 1
        elif start < end:
            count += left_combo
            if start + left_bracket > end:
                # print(i, start, left_bracket, end, left_combo, count)
                count += end - start
                left_bracket = start + left_bracket - end
                left_combo = 1
                # print(i, start, left_bracket, end, left_combo, count)
            else:
                left = end - start
                count += left_bracket
                left -= left_bracket
                if left == 0 and not left_brackets:
                    left_combo = 1
                    left_bracket = 0
                while left_brackets:
                    left_bracket, left_combo = left_brackets.pop()
                    count += left_combo
                    # print(left_bracket, left_combo, left)
                    if left == 0:
                        left_combo += 1
                        break
                    if left_bracket > left:
                        count += left
                        left_bracket -= left
                        left = 0
                        break
                    else:
                        count += left_bracket
                        left -= left_bracket
                        if left == 0 and not left_brackets:
                            left_combo = 1
                            left_bracket = 0

                if left > 0:
                    left_bracket = 0
                    left_combo = 0
        # print(i, count, left_brackets, left_bracket, left_combo)
    return count


def main():
    n = int(parse_input())
    array = [int(i) for i in parse_input().split()]
    print(func(n, array))


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

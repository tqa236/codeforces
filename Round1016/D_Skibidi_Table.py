#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def get_number(n, x, y):
    if n == 1:
        return [[1, 4], [3, 2]][x][y]

    half = 1 << (n - 1)
    block_size = 1 << (2 * (n - 1))

    if x < half and y < half:
        return get_number(n - 1, x, y)
    elif x >= half and y >= half:
        return block_size + get_number(n - 1, x - half, y - half)
    elif x >= half and y < half:
        return 2 * block_size + get_number(n - 1, x - half, y)
    else:
        return 3 * block_size + get_number(n - 1, x, y - half)


def get_position(n, d):
    if n == 1:
        pos = {1: (0, 0), 4: (0, 1), 3: (1, 0), 2: (1, 1)}
        return pos[d]

    block_size = 1 << (2 * (n - 1))

    if d <= block_size:
        x, y = get_position(n - 1, d)
        return x, y
    elif d <= 2 * block_size:
        x, y = get_position(n - 1, d - block_size)
        return x + (1 << (n - 1)), y + (1 << (n - 1))
    elif d <= 3 * block_size:
        x, y = get_position(n - 1, d - 2 * block_size)
        return x + (1 << (n - 1)), y
    else:
        x, y = get_position(n - 1, d - 3 * block_size)
        return x, y + (1 << (n - 1))


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n = int(parse_input())
        q = int(parse_input())
        for __ in range(q):
            array = [i for i in parse_input().split()]
            if array[0] == "->":
                x, y = [int(i) for i in array[1:]]
                result.append(get_number(n, x - 1, y - 1))
            else:
                d = int(array[1])
                x, y = get_position(n, d)
                result.append(f"{x + 1} {y + 1}")

        # result.append(func(n, array))
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

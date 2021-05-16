#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(n, array):
    occupied = []
    empty = []
    count = 0
    for i, val in enumerate(array):
        # print("start", i, val, occupied, empty, count)
        if val == 1:
            occupied.append(i)
        else:
            if not occupied:
                empty.append(i)
            elif empty:
                closest = occupied[0]
                closest_empty = empty[-1]
                index = -1
                for j in range(len(empty) - 1, -1, -1):
                    if abs(empty[j] - closest) <= abs(closest - closest_empty):
                        closest_empty = empty[j]
                        index = j
                    else:
                        break
                # print(i, closest, closest_empty)
                while abs(i - closest) >= abs(closest - closest_empty):
                    count += abs(closest - closest_empty)
                    # print("inc", closest, closest_empty, index, count, empty, occupied)
                    if index < 0:
                        empty.pop()
                    else:
                        empty.pop(index)
                    occupied.pop(0)
                    if not empty or not occupied:
                        break
                    closest = occupied[0]
                    closest_empty = empty[-1]
                    index = -1
                    for j in range(len(empty) - 1, -1, -1):
                        if abs(empty[j] - closest) <= abs(closest - closest_empty):
                            closest_empty = empty[j]
                            index = j
                        else:
                            # print("break")
                            break
                #     print(
                #         "after", closest, closest_empty, index, count, empty, occupied
                #     )
                # print(i, closest, closest_empty, count, occupied, empty)
                empty.append(i)
                # if occupied:
                #     closest = occupied.pop()
                #     count += abs(i - closest)
                # else:
                #     empty.append(i)
            else:
                closest = occupied.pop(0)
                count += abs(i - closest)
        # print("end", i, val, occupied, empty, count)
    # print(empty, occupied)
    while occupied:
        closest = occupied.pop()
        closest_empty = empty.pop()
        count += abs(closest - closest_empty)
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

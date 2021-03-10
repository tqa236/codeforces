#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(array):
    up_first = array[0] < array[1]
    all_changes = []
    curr_up = up_first
    counter = 0
    for i in range(len(array) - 1):
        if curr_up:
            if array[i] < array[i + 1]:
                counter += 1
            else:
                all_changes.append(counter)
                counter = 1
                curr_up = False
        else:
            if array[i] > array[i + 1]:
                counter += 1
            else:
                all_changes.append(counter)
                counter = 1
                curr_up = True
    if counter > 0:
        all_changes.append(counter)
    if len(all_changes) == 1:
        return 0
    # print(all_changes)
    max_change = max(all_changes)
    max_change_indices = [i for i, val in enumerate(all_changes) if val == max_change]
    # print(max_change_indices)
    # print("Here")
    if len(max_change_indices) > 4:
        return 0
    if len(max_change_indices) == 4:
        # print(up_first)
        if not up_first:
            if max_change_indices[3] - max_change_indices[0] == 3:
                if max_change % 2 == 1:
                    return 0
                else:
                    return 1

            return 1
        return 0
    if len(max_change_indices) == 3:
        if up_first:
            return 1
        return 1 if max_change_indices[2] - max_change_indices[0] == 2 else 0
    if len(max_change_indices) == 2:
        return 1 if up_first else 0
    max_change_index = max_change_indices[0]
    if max_change_index % 2 == 0:
        min_val = all_changes[max_change_index + 1]
    else:
        min_val = all_changes[max_change_index - 1]
    max_val = max_change
    # print(min_val, max_val)
    if max_val % 2 == 0:
        max_val -= 1
    # print(min_val, max_val)
    if min_val + 1 >= max_val:
        return 0
    return 1


def main():
    n = int(parse_input())
    array = [int(i) for i in parse_input().split()]
    print(func(array))


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
#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter
import itertools


def func(n, m, array):
    all_paths = list(itertools.chain.from_iterable(array))
    sorted_path = sorted(range(len(all_paths)), key=lambda k: all_paths[k])
    choosing = {}
    choosing_list = []
    indices = [0] * n
    for val in sorted_path[:m]:
        path = val // m
        pos = val % m
        choosing_list.append((path, pos))
        if path in choosing:
            choosing[path].add(pos)
        else:
            choosing[path] = set([pos])
    shorted_paths = []
    # print(array)
    # print(choosing)
    for i in range(m):
        curr = [None] * n
        path, pos = choosing_list[i]
        curr[path] = array[path][pos]
        # print(path, pos, curr)
        for j in range(n):
            if curr[j] is None:
                while j in choosing and indices[j] in choosing[j]:
                    indices[j] += 1
                # print(indices)
                # print(indices[j])
                curr[j] = array[j][indices[j]]
                indices[j] += 1
        shorted_paths.append(curr)
        # print(curr, indices)
        # print(indices)
    # print(all_paths)
    # print(sorted_path)
    # print(choosing)
    shorted_paths = list(map(list, zip(*shorted_paths)))
    # print(shorted_paths)
    for path in shorted_paths:
        print(" ".join(str(i) for i in path))
    # return [" ".join(str(i) for i in path) for path in shorted_paths]


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n, m = [int(i) for i in parse_input().split()]
        array = []
        for i in range(n):
            array.append([int(i) for i in parse_input().split()])
        func(n, m, array)
    # print("\n".join(map(str, result)))


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
#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter

# from itertools import combinations


# def sub_lists(my_list):
#     subs = []
#     for i in range(0, len(my_list) + 1):
#         temp = [list(x) for x in combinations(my_list, i)]
#         if len(temp) > 0:
#             subs.extend(temp)
#     return subs


def func(array, edges):
    u, v = array
    if u > v:
        return "NO"
    to_visit = set([u])
    tmp = v
    count = 0
    while tmp % 2 == 0:
        tmp = tmp // 2
        count += 1
    value = 2 ** (count + 1)
    while to_visit:
        node = to_visit.pop()
        # print(node)
        if node not in edges:
            candidates = set([node + i for i in range(node + 1) if node & i == i])
            edges[node] = candidates
            # print(node, candidates)

        if v in edges[node]:
            return "YES"
        new_nodes = [i for i in edges[node] if i < v and i > node and i % value != 0]
        to_visit.update(new_nodes)
    return "NO"

    # u, v = array
    # if u > v:
    #     return "NO"
    # if u == v:
    #     return "YES"
    # to_visit = set([u])
    # tmp = v
    # count = 0
    # while tmp % 2 == 0:
    #     tmp = tmp // 2
    #     count += 1
    # value = 2 ** (count + 1)
    # node = u
    # while node < v:
    #     for i in range(node, -1, -1):
    #         if node & i == i and i % value != 0:
    #             candidate = node + i
    #             print(node, candidate)
    #             if candidate == v:
    #                 return "YES"
    #             if candidate < v:
    #                 node = candidate
    #                 break
    #         if i == 0:
    #             return "NO"
    # return "NO"


def main():
    num_test = int(parse_input())
    edges = {}
    for _ in range(num_test):
        array = [int(i) for i in parse_input().split()]
        print(func(array, edges))
        # print(edges)


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
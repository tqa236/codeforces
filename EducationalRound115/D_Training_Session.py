#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter
from itertools import combinations
import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom


def func(n, topics, difficulties):
    count = ncr(n, 3)
    # count = 0
    # for a, b, c in combinations(topics.keys(), 3):
    #     count += len(topics[a]) * len(topics[b]) * len(topics[c])
    # for a, b, c in combinations(difficulties.keys(), 3):
    #     count += len(difficulties[a]) * len(difficulties[b]) * len(difficulties[c])
    # print(count)
    for value in topics.values():
        if len(value) == 1:
            continue
        # if len(value) >= 3:
        #     count -= ncr(len(value), 3)
        for a, b in combinations(value, 2):
            # count -= n - len(difficulties[a]) - len(difficulties[b])
            count -= len(difficulties[a]) + len(difficulties[b]) - 2
            # print(a, b, count)
    # print(count)
    # for difficulty, value in difficulties.items():
    #     if len(value) == 1:
    #         continue
    #     if len(value) >= 3:
    #         count -= ncr(len(value), 3)
    #     for a, b in combinations(value, 2):
    #         count -= n - len(topics[a]) - len(topics[b])
    #         # count -= len(topics[a]) + len(topics[b]) - 2
    #         # if difficulty in topics[a]:
    #         #     count += 1
    #         # if difficulty in topics[b]:
    #         #     count += 1
    #         print(a, b, count)
    # print(count)
    # print()
    return count


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n = int(parse_input())
        topics = {}
        difficulties = {}
        for i in range(n):
            topic, difficulty = [int(i) for i in parse_input().split()]
            if topic in topics:
                topics[topic].add(difficulty)
            else:
                topics[topic] = set([difficulty])
            if difficulty in difficulties:
                difficulties[difficulty].add(topic)
            else:
                difficulties[difficulty] = set([topic])
        result.append(func(n, topics, difficulties))
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

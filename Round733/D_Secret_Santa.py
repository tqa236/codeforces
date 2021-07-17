#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter
import random
from itertools import permutations

# random.seed(236)


def func(n, array):
    good = [False] * n
    counter = {}
    for i, val in enumerate(array):
        if val not in counter:
            counter[val] = set([i + 1])
        else:
            counter[val].add(i + 1)
    result = [None] * n
    keys = []
    for key, val in counter.items():
        if len(val) == 1:
            result[list(val)[0] - 1] = key
        else:
            keys.append(key)
    # print(result)
    # print(counter)
    count = 0
    while True:
        result2 = result.copy()
        left = []
        for key in keys:
            choice = random.choice(list(counter[key]))
            result2[choice - 1] = key
        left = list(set(range(1, n + 1)) - set([i for i in result2 if i is not None]))
        # print(result2, left)
        random.shuffle(left)
        # print(left)
        index = 0
        flag = True
        for i in range(n):
            if result2[i] is None:
                if i != left[index] - 1:
                    result2[i] = left[index]
                    index += 1
                else:
                    flag = False
                    break
        if flag:  # or count == 10:
            break
        count += 1
    print(sum(a == b for a, b in zip(array, result2)))
    print(" ".join(map(str, result2)))


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n = int(parse_input())
        array = [int(i) for i in parse_input().split()]
        func(n, array)


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()

#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter

# from icecream import ic

# ic.disable()


def func(n, array, array2):
    if sum(array) != sum(array2):
        print(-1)
        return
    aboves = []
    belows = []
    for i in range(n):
        if array[i] > array2[i]:
            aboves.append(i)
        elif array[i] < array2[i]:
            belows.append(i)
    above = 0
    below = 0
    ops = []
    while above < len(aboves) and below < len(belows):
        ops.append((aboves[above] + 1, belows[below] + 1))
        array[belows[below]] += 1
        array[aboves[above]] -= 1
        if array[belows[below]] == array2[belows[below]]:
            below += 1
        if array[aboves[above]] == array2[aboves[above]]:
            above += 1
    print(len(ops))
    for op in ops:
        print(op[0], op[1])


def main():
    num_test = int(parse_input())
    for _ in range(num_test):
        n = int(parse_input())
        array = [int(i) for i in parse_input().split()]
        array2 = [int(i) for i in parse_input().split()]
        func(n, array, array2)


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

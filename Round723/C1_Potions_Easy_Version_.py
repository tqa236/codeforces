#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter
import bisect


def func(n, array):
    count = 0
    max_count = 0
    neg = []
    health = 0
    for i, val in enumerate(array):
        if val >= 0:
            health += val
            count += 1
        else:
            # print(neg)
            if health + val >= 0:
                health += val
                neg.append(-val)
                # bisect.insort(neg, -val)
                count += 1
                # print(i, val, health)
            else:
                max_count = max(max_count, count)
                health += val
                # bisect.insort(neg, -val)
                neg.append(-val)
                neg = sorted(neg)
                count += 1
                while health < 0:
                    if not neg:
                        return max_count
                    max_neg = neg.pop()
                    # print(neg)
                    health += max_neg
                    # print(health)
                    count -= 1
                # print(health)
    return max(max_count, count)


def main():
    n = int(parse_input())
    array = [int(i) for i in parse_input().split()]
    print(func(n, array))


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

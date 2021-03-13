#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter
import bisect


def lcm(a, b):
    return a * b // math.gcd(a, b)


def func(n, m, k, first, second):
    least = lcm(n, m)
    max_same = len(set(first).intersection(set(second)))
    day = day_diff = same = 0
    same_day = []
    last_diff = 0
    while day_diff < k:
        if first[day % n] != second[day % m]:
            day_diff += 1
            last_diff = day
        else:
            same += 1
            same_day.append(day)
        day += 1
        if day == least or same == max_same:
            if day == least:
                diff_one = day_diff
            else:
                diff_one = least - max_same
            day = least * (k // diff_one)
            day_diff = diff_one * (k // diff_one)
            break
    if not same_day:
        return k
    if day_diff == k:
        if same_day[-1] != least - 1:
            return day
        return day - (least - last_diff - 1)

    same_day.append(least)
    for i, s in enumerate(same_day):
        if s - i >= k - day_diff
            return day + same_day[i - 1] + k - (day_diff + same_day[i - 1] - i)


def main():
    n, m, k = [int(i) for i in parse_input().split()]
    first = [int(i) for i in parse_input().split()]
    second = [int(i) for i in parse_input().split()]
    # n, m, k = 500000, 500000 - 1, 10 ** 12
    # first = list(range(1, n + 1))
    # second = list(range(1, m + 1))
    print(func(n, m, k, first, second))


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
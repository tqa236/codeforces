#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase


def func(x, y):
    count = 0
    b = y
    if x == 1 and y == 1:
        return 0
    if b >= x:
        b = x
    tmp = x // b + 1
    while b > 0:
        for remainder in range(min(b - 1, tmp), 0, -1):
            if b * remainder + remainder <= x:
                if remainder == b - 1:
                    count += b * (b - 1) // 2
                    return count
                count += remainder
                break
        new_b = x // tmp
        if new_b < b:
            count += (b - new_b - 1) * (tmp - 1)
            b = new_b
            tmp += 1
        else:
            b -= 1
    return count


def main():
    num_test = int(parse_input())
    for _ in range(num_test):
        x, y = [int(i) for i in parse_input().split()]
        print(func(x, y))


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
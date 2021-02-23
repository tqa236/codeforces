#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase


def lcs(X, Y):
    m = len(X)
    n = len(Y)

    L = [[0] * 2 for i in range(m + 1)]
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if X[i - 1] == Y[j - 1]:
                L[i][j % 2] = L[i - 1][(j - 1) % 2] + 1
            else:
                L[i][j % 2] = max(L[i - 1][j % 2], L[i][(j - 1) % 2])
    array = [L[i][n % 2] for i in range(1, m + 1)]
    max_width = 0
    start = 0
    old_value = 0
    for i in range(m):
        if array[i] != old_value:
            start = i
            old_value = array[i]
        max_width = max(max_width, i - start + 1)
    # print(L)
    # print(array)
    return max_width


def main():
    m, n = [int(i) for i in parse_input().split()]
    X = parse_input()
    Y = parse_input()
    X = [ord(c) for c in X]
    Y = [ord(c) for c in Y]
    print(lcs(X, Y))


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
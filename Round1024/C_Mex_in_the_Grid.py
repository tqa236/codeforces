import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter
from functools import lru_cache


@lru_cache(100)
def create_grid(n):
    if n == 1:
        return [[0]]

    smaller_grid = create_grid(n - 1)

    grid = [[0] * n for _ in range(n)]

    if n % 2 == 0:
        for i in range(n - 1):
            for j in range(n - 1):
                grid[i][j] = smaller_grid[i][j]
    else:
        for i in range(n - 1):
            for j in range(n - 1):
                grid[i + 1][j + 1] = smaller_grid[i][j]

    value = n * n - 1

    if n % 2 == 0:
        grid[n - 1][n - 1] = value
        value -= 1
        for j in range(n - 1):
            grid[n - 1][j] = value
            value -= 1
        for i in range(n - 1):
            grid[i][n - 1] = value
            value -= 1
    else:
        grid[0][0] = value
        value -= 1
        for i in range(1, n):
            grid[n - i][0] = value
            value -= 1
        for j in range(1, n):
            grid[0][n - j] = value
            value -= 1

    return grid


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


def main():
    num_test = int(parse_input())
    output = []

    for _ in range(num_test):
        n = int(parse_input())
        grid = create_grid(n)
        for row in grid:
            print(" ".join(map(str, row)))
    #     output.append("\n".join(" ".join(map(str, row)) for row in grid))
    # print("\n".join(output) + "\n")


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


if __name__ == "__main__":
    main()

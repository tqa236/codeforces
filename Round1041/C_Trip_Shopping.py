#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        min_max_change = float("inf")
        best_i = None
        best_j = None
        best_sorted = None
        break_outer_loop = False
        for i in range(n):
            for j in range(i + 1, n):
                unchanged_sum = abs(a[i] - b[i]) + abs(a[j] - b[j])
                sorted_values = sorted([a[i], a[j], b[i], b[j]])
                new_change = abs(sorted_values[3] - sorted_values[0]) + abs(
                    sorted_values[2] - sorted_values[1]
                )
                # print(
                #     f"i: {i}, j: {j}, sorted_values: {sorted_values}, new_min_max_change: {new_min_max_change}"
                # )
                if new_change == unchanged_sum:
                    min_max_change = new_change - unchanged_sum
                    best_i = i
                    best_j = j
                    best_sorted = sorted_values
                    break_outer_loop = True
                    break
                if new_change - unchanged_sum < min_max_change:
                    min_max_change = new_change - unchanged_sum
                    best_i = i
                    best_j = j
                    best_sorted = sorted_values
            if break_outer_loop:
                break

        # result = min_max_change
        a[best_i], a[best_j], b[best_i], b[best_j] = best_sorted
        result = 0
        for i in range(n):
            # if i == best_i or i == best_j:
            #     continue
            result += abs(a[i] - b[i])

        print(result)


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

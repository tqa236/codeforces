#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(array):
    n = len(array)
    counter = Counter(array)
    if counter.most_common(1)[0][1] >= 4:
        val = counter.most_common(1)[0][0]
        print("YES")
        val_index = []
        for i in range(n):
            if array[i] == val:
                val_index.append(i)
                if len(val_index) == 4:
                    break
        print(" ".join([str(v + 1) for v in val_index]))
        return

    all_sum = {}
    for i in range(n):
        for j in range(i + 1, n):
            # print(i, j)
            curr_sum = array[i] + array[j]
            if curr_sum in all_sum:
                for curr in all_sum[curr_sum]:
                    if set([i, j]).intersection(set(curr)) == set():
                        print("YES")
                        good_array = [i, j] + curr
                        print(" ".join([str(v + 1) for v in good_array]))
                        return
                    # print(all_sum)
                all_sum[curr_sum].append([i, j])
            else:
                all_sum[curr_sum] = [[i, j]]
    print("NO")


def main():
    n = int(parse_input())
    array = [int(i) for i in parse_input().split()]
    func(array)


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

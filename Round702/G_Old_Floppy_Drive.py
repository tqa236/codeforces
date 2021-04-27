#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math


def func(array, queries):
    presum = []
    for i in array:
        if not presum:
            presum.append(i)
        else:
            presum.append(presum[-1] + i)
    inc = presum[-1]
    caches = {}
    time = []
    length = len(array)
    for query in queries:
        if query in caches:
            time.append(caches[query])
        else:
            min_time = float("inf")
            for i, d in enumerate(presum):
                if query >= d:
                    min_time = i
                    time.append(min_time)
                break
            if min_time == float("inf"):
                if query in presum:
                    min_time = presum.index(query)
                elif inc == 0:
                    min_time = -1
                else:
                    min_time = float("inf")
                    for index, val in enumerate(presum):
                        run = (query - val) / inc
                        # print(run)
                        if run >= 0:
                            min_time = min(
                                min_time, index + length * int(math.ceil(run))
                            )
                    if min_time == float("inf"):
                        min_time = -1
                caches[query] = min_time
                time.append(min_time)
    return " ".join([str(i) for i in time])


def main():
    num_test = int(parse_input())
    for _ in range(num_test):
        n, m = [int(i) for i in parse_input().split()]
        array = [int(i) for i in parse_input().split()]
        queries = [int(i) for i in parse_input().split()]
        print(func(array, queries))


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

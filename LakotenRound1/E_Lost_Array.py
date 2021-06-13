#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(n, k):
    val = 0
    array = list(range(1, n + 1))
    if n % 2 != 0 and k % 2 == 0:
        print(-1)
        return
    left = n % k
    if left != 0:
        gcd = math.gcd(left, k)
        new_left = left // gcd
        new_k = k // gcd
        if new_left % 2 != 0 and new_k % 2 == 0:
            print(-1)
            return
    group = n // k
    for i in range(group):
        curr = array[i * k : (i + 1) * k]
        curr_str = " ".join(str(j) for j in curr)
        print(f"? {curr_str}")
        sys.stdout.flush()
        result = int(parse_input())
        val = val ^ result
    if left == 0:
        print(f"! {val}")
        return
    left_index = array[-left:]
    num_sub = k // gcd
    num_left = left // gcd
    subs = []
    lefts = []
    for i in range(num_sub):
        subs.append(array[gcd * i : gcd * (i + 1)])

    # print(left_index, subs)
    for i in range(num_sub):
        query = [y for j, x in enumerate(subs) for y in x if j != i] + left_index
        curr_str = " ".join(str(j) for j in query)
        print(f"? {curr_str}")
        sys.stdout.flush()
        result = int(parse_input())
        val = val ^ result
    print(f"! {val}")
    return


def main():
    n, k = [int(i) for i in parse_input().split()]
    func(n, k)


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

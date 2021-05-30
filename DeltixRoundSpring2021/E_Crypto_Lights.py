#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter

CACHES = {}
M = 10 ** 9 + 7


def add(a, b):
    top = a[0] * b[1] + b[0] * a[1]
    bottom = a[1] * b[1]
    gcd_val = math.gcd(top, bottom)
    return (top // gcd_val, bottom // gcd_val)


def mul(a, b):
    if isinstance(a, int):
        a = (a, 1)
    top = a[0] * b[0]
    bottom = a[1] * b[1]
    gcd_val = math.gcd(top, bottom)
    return (top // gcd_val, bottom // gcd_val)


def prob(n, k, max_choice):
    if (n, k) in CACHES:
        return CACHES[(n, k)]
    if n <= 0:
        return (0, 1)
    if n == 1:
        return (1, 1)
    if n <= k:
        return (2, 1)
    expectation = (0, 1)
    for i in range((n + 1) // 2):
        if i <= k - 1:
            left_len = 0
        else:
            left_len = i - k + 1
        if i + k >= n:
            right_len = 0
        else:
            right_len = n - i - k
        center_len = n - left_len - right_len
        print(i, n, k, left_len, center_len, right_len)
    #     left = prob(left_len, k)
    #     center = prob(center_len, k)
    #     right = prob(right_len, k)
    #     print(left, center, right)
    #     local_expectation = (0, 1)
    #     print(local_expectation)
    #     local_expectation = add(local_expectation, mul((left_len, n - 1), left))
    #     print(local_expectation)
    #     local_expectation = add(local_expectation, mul((center_len, n - 1), center))
    #     print(local_expectation)
    #     local_expectation = add(local_expectation, mul((right_len, n - 1), right))
    #     print(local_expectation)

    #     local_expectation = mul((2, n - 1), local_expectation)
    #     print(local_expectation)
    #     expectation = add(expectation, local_expectation)
    # print(expectation)
    # CACHES[(n, k)] = expectation
    return expectation


def func(array):
    n, k = array
    p, q = prob(n, k, n)
    for i in range(M):
        if (i * q - p) % M == 0:
            return i


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        array = [int(i) for i in parse_input().split()]
        result.append(func(array))
    print("\n".join(map(str, result)))


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

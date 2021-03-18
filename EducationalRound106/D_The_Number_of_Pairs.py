#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter

PRIMES = set([3])


def primeFactors(n):
    if n == 1:
        return Counter({})
    exponents = {}
    count = 0
    while n % 2 == 0:
        count += 1
        n = n // 2
    exponents[2] = count
    for i in PRIMES:
        count = 0
        while n % i == 0:
            count += 1
            n = n // i
        exponents[i] = count
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if i in exponents:
            continue
        count = 0
        while n % i == 0:
            count += 1
            n = n // i
        exponents[i] = count
        if count > 0:
            PRIMES.add(i)
    if n > 2:
        exponents[n] = 1
        PRIMES.add(n)
    # print(PRIMES)
    return Counter(exponents)


def printDivisors(n):
    all_div = set()
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            if n == i * i:
                all_div.add(i)
            else:
                all_div.add(i)
                all_div.add(n // i)
        i = i + 1
    return all_div


def countPairs(k):
    factors = len([factor for factor, value in primeFactors(k).items() if value > 0])
    return 2 ** factors


def func(array):
    caches = {}
    count = 0
    c, d, x = array
    g = math.gcd(c, d)
    if x % g != 0:
        return 0
    c, d, x = c // g, d // g, x // g
    all_div = printDivisors(x)
    for y0 in all_div:
        tmp = y0 + d
        if tmp % c == 0:
            k = tmp // c
            if k not in caches:
                caches[k] = countPairs(k)
            count += caches[k]
    return count


def main():
    num_test = int(parse_input())
    for _ in range(num_test):
        array = [int(i) for i in parse_input().split()]
        print(func(array))


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
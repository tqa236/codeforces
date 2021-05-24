#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter

MODULO = 998244353
MAX_PRIME = 3
PRIMES = set([3])
DIVISORS = {1: 1, 2: 2}

# EXPONENTS = {1: Counter({})}
#


# def primeFactors(n):
#     global MAX_PRIME
#     org_n = n
#     if n == 1:
#         return Counter({})
#     exponents = {}
#     count = 0
#     while n % 2 == 0:
#         count += 1
#         n = n // 2
#     if count > 0:
#         exponents[2] = count
#         if n in EXPONENTS:
#             EXPONENTS[org_n] = Counter(exponents) + EXPONENTS[n]
#             return EXPONENTS[org_n]
#     for i in PRIMES:
#         count = 0
#         while n % i == 0:
#             count += 1
#             n = n // i
#         if count > 0:
#             exponents[i] = count
#             if n in EXPONENTS:
#                 EXPONENTS[org_n] = Counter(exponents) + EXPONENTS[n]
#                 return EXPONENTS[org_n]
#     for i in range(MAX_PRIME + 1, int(math.sqrt(n)) + 1, 2):
#         count = 0
#         while n % i == 0:
#             count += 1
#             n = n // i
#         if count > 0:
#             exponents[i] = count
#             PRIMES.add(i)
#             MAX_PRIME = max(MAX_PRIME, i)
#             if n in EXPONENTS:
#                 EXPONENTS[org_n] = Counter(exponents) + EXPONENTS[n]
#                 return EXPONENTS[org_n]
#     if n > 2:
#         exponents[n] = 1
#         PRIMES.add(n)
#         MAX_PRIME = max(MAX_PRIME, n)
#     EXPONENTS[org_n] = Counter(exponents)
#     return EXPONENTS[org_n]


def count_divisor(n):
    global MAX_PRIME
    org_n = n
    if n == 1:
        return 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n // 2
    if count > 0:
        DIVISORS[org_n] = DIVISORS[n] * (count + 1) % MODULO
        return DIVISORS[org_n]
    for i in PRIMES:
        count = 0
        while n % i == 0:
            count += 1
            n = n // i
        if count > 0:
            DIVISORS[org_n] = DIVISORS[n] * (count + 1) % MODULO
            return DIVISORS[org_n]
    for i in range(MAX_PRIME + 1, int(math.sqrt(n)) + 1, 2):
        count = 0
        while n % i == 0:
            count += 1
            n = n // i
        if count > 0:
            PRIMES.add(i)
            MAX_PRIME = max(MAX_PRIME, i)
            DIVISORS[org_n] = DIVISORS[n] * (count + 1) % MODULO
            return DIVISORS[org_n]
    if n > 2:
        PRIMES.add(n)
        MAX_PRIME = max(MAX_PRIME, n)
        DIVISORS[org_n] = 2
    return DIVISORS[org_n]


def func(n):
    if n == 1:
        return 1
    mem = [0 for i in range(int(1e6) + 1)]
    tot = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            mem[j] += 1

        mem[i] += mem[i - 1] + tot
        mem[i] %= MODULO

        tot += mem[i - 1]
        tot %= MODULO

    ans = mem[n]
    ans %= MODULO
    return ans


def main():
    n = int(parse_input())
    print(func(n))


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

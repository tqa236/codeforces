#!/usr/bin/env python
import os
import sys
from math import gcd
import math
from io import BytesIO, IOBase

import copy


def generate_primes_upto(n: int):
    if n < 2:
        return []

    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"

    limit = int(math.isqrt(n))
    for p in range(2, limit + 1):
        if sieve[p]:
            start = p * p
            step = p
            sieve[start : n + 1 : step] = b"\x00" * ((n - start) // step + 1)

    return [i for i in range(n + 1) if sieve[i]]


PRIMES = generate_primes_upto(10**5)[::-1]


def lcm(x, y):
    if x == 0 or y == 0:
        return 0
    return (x * y) // gcd(x, y)


def func(n, a, b):
    E = [1] * (n + 1)
    for i in range(1, n):
        E[i] = gcd(a[i - 1], a[i])

    G = [1] * n
    for i in range(n):
        G[i] = lcm(E[i], E[i + 1])

    ans = 0

    candidates = []
    og_a = copy.deepcopy(a)
    for i in range(n):
        if G[i] > b[i]:
            continue
        if G[i] != a[i]:
            ans += 1
            a[i] = G[i]
        else:
            a[i] = G[i]
            limit = b[i] // G[i]
            if limit >= 2:
                candidates.append((limit, i))
    if not candidates:
        return ans

    candidates.sort(key=lambda x: x[0], reverse=True)

    p_start_index = 0
    for limit, i in candidates:
        for p_index in range(p_start_index, len(PRIMES)):
            p = PRIMES[p_index]
            if p > limit:
                p_start_index += 1
                continue
            v_prev = 0 if i == 0 else (1 if (a[i - 1] // E[i]) % p == 0 else 0)
            v_next = 0 if i == n - 1 else (1 if (a[i + 1] // E[i + 1]) % p == 0 else 0)
            v_curr = 1 if G[i] * p == og_a[i] else 0

            if v_prev == 0 and v_next == 0 and v_curr == 0:
                ans += 1
                a[i] = G[i] * p

                break

    return ans


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
    parse_input = lambda: sys.stdin.readline().rstrip("\r\n")
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n = int(parse_input())
        array_a = [int(i) for i in parse_input().split()]
        array_b = [int(i) for i in parse_input().split()]
        result.append(func(n, array_a, array_b))
    print("\n".join(map(str, result)))


if __name__ == "__main__":
    main()

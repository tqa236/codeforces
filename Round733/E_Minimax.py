#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter

# from icecream import ic

# ic.disable()

m = 31607


# Function to return the GCD
# of given numbers
def gcd(a, b):

    if a == 0:
        return b
    return gcd(b % a, a)


# Recursive function to return (x ^ n) % m
def modexp(x, n):

    if n == 0:
        return 1

    elif n % 2 == 0:
        return modexp((x * x) % m, n // 2)

    else:
        return x * modexp((x * x) % m, (n - 1) / 2) % m


# Function to return the fraction modulo mod
def getFractionModulo(a, b):

    c = gcd(a, b)

    a = a // c
    b = b // c

    # (b ^ m-2) % m
    d = modexp(b, m - 2)

    # Final answer
    ans = ((a % m) * (d % m)) % m

    return ans


def func(array):
    print(getFractionModulo(11, 16))
    pass


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        array = parse_input()
        result.append(func(array))
    print("\n".join(map(str, result)))


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

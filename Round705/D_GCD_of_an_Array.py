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


def gcd(all_exponents):
    curr = all_exponents[0]
    for exponents in all_exponents[1:]:
        for factor, count in exponents.items():
            if factor in curr:
                curr[factor] = min(count, curr[factor])
            else:
                curr[factor] = 0
    return curr


def gcd_num(exponents):
    num = 1
    for factor, count in exponents.items():
        num *= factor ** count
    return num


def func(q, array):
    all_exponents = [primeFactors(n) for n in array]
    curr_gcd = gcd(all_exponents)
    curr_gcd_num = gcd_num(curr_gcd)
    # print(all_exponents)
    # print(curr_gcd)
    for _ in range(q):
        increase = 1
        i, x = [int(i) for i in parse_input().split()]
        i -= 1
        # print(i, x)

        new_val = Counter(primeFactors(x))
        new_factors = new_val.keys()
        changed = []
        for factor in new_factors:
            if (
                factor not in all_exponents[i]
                or factor not in curr_gcd
                or all_exponents[i][factor] <= curr_gcd[factor]
            ):
                changed.append(factor)
        all_exponents[i] = all_exponents[i] + new_val
        # print(new_factors)
        # print(all_exponents)
        # print(changed)
        for factor in changed:
            if factor not in curr_gcd:
                curr_gcd[factor] = 0
            min_val = float("inf")
            update = True
            for exponents in all_exponents:
                if factor not in exponents:
                    update = False
                    break
                if exponents[factor] < min_val:
                    min_val = exponents[factor]
            if update:
                increase *= factor ** (min_val - curr_gcd[factor])
                curr_gcd[factor] = min_val
        curr_gcd_num *= increase
        # print(curr_gcd)
        print(curr_gcd_num % (10 ** 9 + 7))


def main():
    n, q = [int(i) for i in parse_input().split()]
    array = [int(i) for i in parse_input().split()]
    func(q, array)


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
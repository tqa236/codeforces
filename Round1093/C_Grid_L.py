#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter

# max_prime = 10**4 + 10000

# sieve = [True] * (max_prime + 2)
# sieve[0] = sieve[1] = False
# for i in range(2, int((max_prime + 1) ** 0.5) + 1):
#     if sieve[i]:
#         sieve[i * i :: i] = [False] * len(sieve[i * i :: i])
# primes = [i for i, is_prime in enumerate(sieve) if is_prime]


def condition(p, q):
    k = p + 2 * q

    for prime in range(3, 10**4 + 10000, 2):
        if prime > (2 * k + 1) ** 0.5:
            return -1
        if (2 * k + 1) % prime == 0:
            value = [(prime - 1) // 2, ((2 * k + 1) // prime - 1) // 2]
            if abs(value[0] - value[1]) > p:
                continue
            if min(value) < 1:
                continue
            return " ".join(map(str, value))
    return -1


def func(p, q):

    return condition(p, q)


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        p, q = [int(i) for i in parse_input().split()]
        result.append(func(p, q))
    print("\n".join(map(str, result)))


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


if __name__ == "__main__":
    main()

#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def min_operations_to_obtain_target(n, m, a, networks):
    dp = [[float("inf")] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = n - 1

    for i in range(n):
        for j in range(n + 1):
            if dp[i][j] == float("inf"):
                continue
            for k in range(m):
                if networks[k][i] == a[i]:
                    if i + 1 <= n and j + 1 <= n:
                        dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + 1)
            if j + 1 <= n:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

    min_ops = min(dp[n])
    return min_ops if min_ops != float("inf") else -1


def func(n, m, a, b):
    # Check for each index i if we can ensure a[i] in the final array
    operations = 0
    can_set = [
        False
    ] * n  # Tracks if the value at index i can be set to a[i] in the end

    # Step 1: For each index in target a, try to find operations that guarantee setting a[i]
    for i in range(n):
        found = False
        for j in range(m):
            if b[j][i] == a[i]:
                found = True
                break
        if not found:
            # No network can guarantee setting a[i], output -1 for this test case
            operations = -1
            break
        operations += 1

    # If we have no solution, just print -1
    if operations == -1:
        return -1
    else:
        return operations


def func2(n, m, a, b):
    operations = 0
    possible = True

    # Check each position in a
    for i in range(n):
        found = False
        # Check if any neural network can provide a[i]
        for j in range(m):
            if b[j][i] == a[i]:
                found = True
                break
        if not found:
            possible = False
            break
        operations += 1

    # If transformation is possible, add the number of operations
    if possible:
        return operations
    else:
        return -1


def func3(n, m, a, b):
    # Track the minimum number of operations
    operations = 0

    # Process each position i of array `a`
    for i in range(n):
        possible = False
        # Check if there's any neural network that can place a[i] in c[i]
        for j in range(m):
            if b[j][i] == a[i]:
                possible = True
                break

        if not possible:
            # If no network can guarantee a[i] at index i
            operations = -1
            break
        # If there's a valid network, we increment the operation count
        operations += 1

    if operations == -1:
        return -1
    else:
        # Now we need to add the reset operations where needed
        for i in range(n):
            can_preserve = False
            for j in range(m):
                if b[j][i] == a[i]:
                    can_preserve = True
                    break
            if not can_preserve:
                # If we cannot preserve the element at `a[i]` from `b` then a reset is required.
                operations += 1

        return operations


def func4(n, m, a, b):
    for i in range(n):
        if not any(network[i] == a[i] for network in b):
            return -1
    max_same = 0
    for j in range(m):
        num_same = sum(1 for i in range(n) if b[j][i] == a[i])
        max_same = max(max_same, num_same)
    # print(max_same)
    return n + 2 * (n - max_same)


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n, m = [int(i) for i in parse_input().split()]
        a = [i for i in parse_input().split()]
        networks = []
        for __ in range(m):
            networks.append([i for i in parse_input().split()])
        result.append(func4(n, m, a, networks))
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

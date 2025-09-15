#!/usr/bin/env python
import sys
from itertools import combinations
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


MOD = 998244353


def func(n, a):
    # Step 1: Get left maxima (L) and right maxima (R) with indices
    L = []
    L_idx = []
    maxL = -1
    for i in range(n):
        if a[i] > maxL:
            maxL = a[i]
            L.append(a[i])
            L_idx.append(i)
    R = []
    R_idx = []
    maxR = -1
    for i in range(n - 1, -1, -1):
        if a[i] > maxR:
            maxR = a[i]
            R.append(a[i])
            R_idx.append(i)
    R = R[::-1]
    R_idx = R_idx[::-1]

    # Step 2: Merge L and R to get the sequence of required maxima, in order, without duplicates
    req_vals = []
    seen = set()
    lp = rp = 0
    while lp < len(L) and rp < len(R):
        if L[lp] == R[rp]:
            if L[lp] not in seen:
                req_vals.append(L[lp])
                seen.add(L[lp])
            lp += 1
            rp += 1
        elif L[lp] < R[rp]:
            if L[lp] not in seen:
                req_vals.append(L[lp])
                seen.add(L[lp])
            lp += 1
        else:
            if R[rp] not in seen:
                req_vals.append(R[rp])
                seen.add(R[rp])
            rp += 1
    while lp < len(L):
        if L[lp] not in seen:
            req_vals.append(L[lp])
            seen.add(L[lp])
        lp += 1
    while rp < len(R):
        if R[rp] not in seen:
            req_vals.append(R[rp])
            seen.add(R[rp])
        rp += 1

    # Step 3: For each block, count options
    # Find all indices for each required value
    val_indices = {}
    for idx, val in enumerate(a):
        val_indices.setdefault(val, []).append(idx)

    # Build blocks: each block is from last boundary to this (inclusive)
    block_bounds = []
    curr = 0
    for v in req_vals:
        indices = val_indices[v]
        # Among indices >= curr, the rightmost to pick for this value is the first that comes after curr
        # The block runs from curr to the last occurrence of v after curr, inclusive
        i = 0
        while i < len(indices) and indices[i] < curr:
            i += 1
        start = curr
        end = indices[-1]  # last occurrence of v at or after curr
        # Actually, end should be up to the last occurrence of v before the next required value (or n-1 for the last one)
        block_bounds.append((start, end, v))
        curr = end + 1

    used_indices = set()
    ans = 1
    for start, end, v in block_bounds:
        cnt = 0
        for i in range(start, end + 1):
            if a[i] == v:
                cnt += 1
                used_indices.add(i)
        ans = ans * ((pow(2, cnt, MOD) - 1) % MOD) % MOD

    # Step 4: Free elements
    free = n - len(used_indices)
    ans = ans * pow(2, free, MOD) % MOD
    return ans


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n = int(parse_input())
        array = [int(i) for i in parse_input().split()]
        result.append(func(n, array))
    print("\n".join(map(str, result)))


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

if __name__ == "__main__":
    main()

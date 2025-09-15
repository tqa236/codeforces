#!/usr/bin/env python3
import sys, math
from collections import Counter

input = sys.stdin.readline


def solve_one(n, y, arr):
    max_c = max(arr)
    old_cnt = Counter(arr)

    candidates = {2, max_c + 1}

    for c in arr:
        k = 1
        while k * k <= c:
            candidates.add((c + k - 1) // k)
            if c // k > 1:
                candidates.add(c // k)
            k += 1

    for x in range(2, int(math.isqrt(max_c)) + 3):
        candidates.add(x)

    best = -(10**30)
    for x in candidates:
        if x <= 1:
            continue
        new_prices = [(c + x - 1) // x for c in arr]
        new_cnt = Counter(new_prices)
        new_sum = sum(new_prices)
        matched = sum(min(old_cnt[v], new_cnt[v]) for v in new_cnt)
        income = new_sum - y * (n - matched)
        if income > best:
            best = income

    return best


def main():
    t = int(input())
    out = []
    for _ in range(t):
        n, y = map(int, input().split())
        arr = list(map(int, input().split()))
        out.append(str(solve_one(n, y, arr)))
    print("\n".join(out))


if __name__ == "__main__":
    main()

import sys
import bisect


def solve(n, array):
    positions = [[] for _ in range(n + 1)]
    for i, num in enumerate(array):
        positions[num].append(i)

    intervals = []
    for x in range(1, n + 1):
        l, r = positions[x]
        span = r - l + 1
        weight = span * (span - 1)
        intervals.append((l, r, weight))

    intervals.sort(key=lambda x: x[1])
    rs = [inter[1] for inter in intervals]

    dp = [0] * (n + 1)
    for i in range(n):
        l_i, r_i, w_i = intervals[i]
        j = bisect.bisect_left(rs, l_i) - 1
        prev_val = dp[j + 1] if j >= 0 else 0
        dp[i + 1] = max(dp[i], prev_val + w_i)

    total_score = dp[n] + 2 * n
    return total_score


def main():
    num_test = int(parse_input())
    results = []
    for _ in range(num_test):
        n = int(parse_input())
        array = list(map(int, parse_input().split()))
        results.append(str(solve(n, array)))
    print("\n".join(results))


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

if __name__ == "__main__":
    main()

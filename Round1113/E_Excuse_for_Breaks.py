import sys
import bisect


def solve(n, m, d, p, r):

    pref_v = [0] * (m + 1)

    for i in range(m):
        pref_v[i + 1] = pref_v[i] + r[i]

    if m == 0:
        return "NO"

    V_n = pref_v[m]
    found = False

    for i in range(m):
        A = p[i]
        vA_minus_d = pref_v[i + 1] - d
        for j in range(m):
            B = p[j]
            target = vA_minus_d + pref_v[j + 1]

            S = A + B + 1

            if S >= 2 * n:
                q = 2
                rem = S - 2 * n
            elif S >= n:
                q = 1
                rem = S - n
            else:
                q = 0
                rem = S

            b_idx = bisect.bisect_right(p, rem)

            if target > q * V_n + pref_v[b_idx]:
                found = True
                break

        if found:
            break

    if found:
        return "YES"
    else:
        return "NO"


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n, m, d = [int(i) for i in parse_input().split()]
        p = []
        r = []
        for _ in range(m):
            p_i, r_i = [int(i) for i in parse_input().split()]
            p.append(p_i)
            r.append(r_i)
        result.append(solve(n, m, d, p, r))
    print("\n".join(map(str, result)))


# sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


if __name__ == "__main__":
    main()

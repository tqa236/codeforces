import sys


def solve(n, q, s, t, queries):
    out = []
    pref_01 = [0] * (n + 1)
    pref_10 = [0] * (n + 1)
    for i in range(n):
        pref_01[i + 1] = pref_01[i]
        pref_10[i + 1] = pref_10[i]
        if s[i] == "0" and t[i] == "1":
            pref_01[i + 1] += 1
        elif s[i] == "1" and t[i] == "0":
            pref_10[i + 1] += 1

    for l, r in queries:
        c_01 = pref_01[r] - pref_01[l - 1]
        c_10 = pref_10[r] - pref_10[l - 1]
        length = r - l + 1

        if 2 * c_01 <= length and 2 * c_10 <= length:
            out.append("YES")
        else:
            out.append("NO")
    return "\n".join(out)


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n, q = [int(i) for i in parse_input().split()]
        s = parse_input()
        t = parse_input()
        queries = []
        for _ in range(q):
            l, r = [int(i) for i in parse_input().split()]
            queries.append((l, r))
        result.append(solve(n, q, s, t, queries))
    print("\n".join(map(str, result)))


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

if __name__ == "__main__":
    main()

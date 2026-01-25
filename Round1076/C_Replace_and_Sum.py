import sys


def parse_input():
    return sys.stdin.readline().strip()


def func(n, a, b, queries):
    c = [max(a[i], b[i]) for i in range(n)]

    for i in range(n - 2, -1, -1):
        c[i] = max(c[i], c[i + 1])

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + c[i]

    result = []
    for l, r in queries:
        l0 = l - 1
        r0 = r - 1
        sum_val = prefix[r0 + 1] - prefix[l0]
        result.append(sum_val)
    return result


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n, q = map(int, parse_input().split())
        a = list(map(int, parse_input().split()))
        b = list(map(int, parse_input().split()))
        queries = []
        for __ in range(q):
            l, r = map(int, parse_input().split())
            queries.append((l, r))
        res = func(n, a, b, queries)
        result.append(" ".join(map(str, res)))
    print("\n".join(result))


if __name__ == "__main__":
    main()

import sys


def solve(n, m, a, b):
    a.sort()
    b.sort()
    if n < 2 * m:
        return "NO"
    ok = True
    for i in range(m):
        if not (a[i] < b[i] and a[n - m + i] > b[i]):
            ok = False
            break
    return "YES" if ok else "NO"


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n, m = [int(i) for i in parse_input().split()]
        a = [int(i) for i in parse_input().split()]
        b = [int(i) for i in parse_input().split()]
        result.append(solve(n, m, a, b))
    print("\n".join(map(str, result)))


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

if __name__ == "__main__":
    main()

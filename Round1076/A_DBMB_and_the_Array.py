import sys


def func(n, s, x, array):
    current_sum = sum(array)
    if s < current_sum:
        return "NO"
    diff = s - current_sum
    if diff % x == 0:
        return "YES"
    else:
        return "NO"


def parse_input():
    return sys.stdin.readline().strip()


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n, s, x = map(int, parse_input().split())
        array = list(map(int, parse_input().split()))
        result.append(func(n, s, x, array))
    print("\n".join(result))


if __name__ == "__main__":
    main()

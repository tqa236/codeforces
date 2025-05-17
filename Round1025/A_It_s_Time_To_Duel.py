import sys

parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def func(n, array):
    if sum(array) == n:
        return "YES"
    if n == 2:
        if array[0] == array[1]:
            return "YES"

    for i in range(n - 1):
        if array[i] == array[i + 1] == 0:
            return "YES"
    return "NO"


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n = int(parse_input())
        array = list(map(int, parse_input().split()))
        result.append(func(n, array))

    sys.stdout.write("\n".join(result) + "\n")


if __name__ == "__main__":
    main()

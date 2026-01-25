import sys


def func(n, array):
    for i in range(n):
        max_val = max(array[i:])

        if array[i] < max_val:
            j = i
            for k in range(i, n):
                if array[k] == max_val:
                    j = k

            result = array[:i] + array[i : j + 1][::-1] + array[j + 1 :]
            return result

    return array


def parse_input():
    return sys.stdin.readline().rstrip()


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n = int(parse_input())
        array = [int(i) for i in parse_input().split()]
        result.append(" ".join(map(str, func(n, array))))
    print("\n".join(result))


if __name__ == "__main__":
    main()

import sys
from collections import deque

parse_input = sys.stdin.readline


def func(n, array):
    distinct_elements = sorted(list(set(array)))

    dist = [-1] * (n + 1)
    queue = deque()
    for x in distinct_elements:
        if x <= n:
            dist[x] = 1
            queue.append(x)

    while queue:
        curr = queue.popleft()
        curr_dist = dist[curr]

        for x in distinct_elements:
            if x == 1:
                continue

            next_val = curr * x
            if next_val > n:
                break

            if dist[next_val] == -1:
                dist[next_val] = curr_dist + 1
                queue.append(next_val)

    return " ".join(map(str, dist[1:]))


def main():
    input_str = parse_input()
    num_test = int(input_str)

    result = []
    for _ in range(num_test):
        n = int(parse_input())
        array = [int(i) for i in parse_input().split()]
        result.append(func(n, array))
    print("\n".join(map(str, result)))


if __name__ == "__main__":
    main()

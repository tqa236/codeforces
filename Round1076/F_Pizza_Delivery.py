import sys


def func(n, ax, ay, bx, by, xs, ys):
    coords = {}
    for i in range(n):
        x, y = xs[i], ys[i]
        if x not in coords:
            coords[x] = [y, y]
        else:
            coords[x][0] = min(coords[x][0], y)
            coords[x][1] = max(coords[x][1], y)

    sorted_x = sorted(coords.keys())

    x0 = sorted_x[0]
    ymin0, ymax0 = coords[x0]

    dist_x = x0 - ax

    dp_ymin = dist_x + abs(ymax0 - ay) + (ymax0 - ymin0)
    dp_ymax = dist_x + abs(ymin0 - ay) + (ymax0 - ymin0)

    prev_x = x0

    for i in range(1, len(sorted_x)):
        curr_x = sorted_x[i]
        ymin, ymax = coords[curr_x]
        dx = curr_x - prev_x

        new_dp_ymin = min(
            dp_ymin + dx + abs(ymax - coords[prev_x][0]) + (ymax - ymin),
            dp_ymax + dx + abs(ymax - coords[prev_x][1]) + (ymax - ymin),
        )

        new_dp_ymax = min(
            dp_ymin + dx + abs(ymin - coords[prev_x][0]) + (ymax - ymin),
            dp_ymax + dx + abs(ymin - coords[prev_x][1]) + (ymax - ymin),
        )

        dp_ymin, dp_ymax = new_dp_ymin, new_dp_ymax
        prev_x = curr_x

    final_dist_x = bx - prev_x
    res = min(
        dp_ymin + final_dist_x + abs(by - coords[prev_x][0]),
        dp_ymax + final_dist_x + abs(by - coords[prev_x][1]),
    )
    return res


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n, ax, ay, bx, by = [int(i) for i in parse_input().split()]
        xs = [int(i) for i in parse_input().split()]
        ys = [int(i) for i in parse_input().split()]
        result.append(func(n, ax, ay, bx, by, xs, ys))
    print("\n".join(map(str, result)))


if __name__ == "__main__":
    main()

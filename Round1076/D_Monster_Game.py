import sys
import bisect


def func(n, swords, monsters):
    swords.sort()

    pref_monsters = [0] * (n + 1)
    for i in range(n):
        pref_monsters[i + 1] = pref_monsters[i] + monsters[i]

    max_score = 0

    for i in range(n):
        if i > 0 and swords[i] == swords[i - 1]:
            continue

        available_strikes = n - i
        difficulty = swords[i]

        levels_completed = bisect.bisect_right(pref_monsters, available_strikes) - 1

        current_score = difficulty * levels_completed
        if current_score > max_score:
            max_score = current_score
    return str(max_score)


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n = int(parse_input())
        swords = [int(i) for i in parse_input().split()]
        monsters = [int(i) for i in parse_input().split()]
        result.append(func(n, swords, monsters))
    print("\n".join(map(str, result)))


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

if __name__ == "__main__":
    main()

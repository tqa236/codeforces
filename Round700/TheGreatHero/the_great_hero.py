import math


def the_great_hero(A, B, attack, health):
    times = [int(math.ceil(h / A)) for h in health]
    hero_health = [time * a for time, a in zip(times, attack)]
    return "YES" if B - sum(hero_health) + max(attack) > 0 else "NO"


if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        A, B, n = [int(i) for i in input().split()]
        attack = [int(i) for i in input().split()]
        health = [int(i) for i in input().split()]
        print(the_great_hero(A, B, attack, health))

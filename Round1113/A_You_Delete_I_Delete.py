import os
import sys


def solve(s: str) -> str:
    first_zero = s.find("0")
    s_after_alice = s[:first_zero] + s[first_zero + 1 :]

    first_one = s_after_alice.find("1")
    s_final = s_after_alice[:first_one] + s_after_alice[first_one + 1 :]

    return s_final


def main():
    parse_input = sys.stdin.read().split()

    t = int(parse_input[0])
    results = []

    for i in range(1, t + 1):
        s = parse_input[i]
        results.append(solve(s))

    print("\n".join(results))


if __name__ == "__main__":
    main()

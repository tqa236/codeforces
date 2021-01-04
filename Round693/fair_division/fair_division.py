from collections import Counter


def is_possible(candies):
    candy_dict = Counter(candies)
    if candy_dict[1] % 2 != 0:
        return False
    if candy_dict[1] == 0 and candy_dict[2] % 2 != 0:
        return False
    return True


if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        num_num = int(input())
        candies = [int(i) for i in input().split()]
        if is_possible(candies):
            print("YES")
        else:
            print("NO")
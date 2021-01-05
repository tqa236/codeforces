import math
from collections import Counter


def strange_birthday_party(friends, presents):
    count = 0
    cost = 0
    friend_counter = Counter(friends)
    use_present = True
    buy_present = 0
    for index in sorted(friend_counter.keys(), reverse=True):
        value = friend_counter[index]
        if use_present and (index > count):
            count += value
            buy_present = count
            if count >= index:
                use_present = False
                cost += presents[index - 1] * (count - index)
                buy_present = index
        else:
            cost += presents[index - 1] * value
    return cost + sum(presents[:buy_present])


if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        n, m = [int(i) for i in input().split()]
        friends = [int(i) for i in input().split()]
        presents = [int(i) for i in input().split()]
        print(strange_birthday_party(friends, presents))
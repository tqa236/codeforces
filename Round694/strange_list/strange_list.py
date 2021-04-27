import math


def strange_list(nums, x):
    x_factor = float("inf")
    x_index = None
    for index, num in enumerate(nums):
        value = 0
        tmp = num
        while tmp % x == 0:
            tmp = tmp / x
            value += 1
        if value < x_factor:
            x_factor = value
            x_index = index
        if value == 0:
            break
    return sum(num * (x_factor + 1) for num in nums) + sum(
        num for num in nums[:x_index]
    )


if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        n, x = [int(i) for i in input().split()]
        nums = [int(i) for i in input().split()]
        print(strange_list(nums, x))

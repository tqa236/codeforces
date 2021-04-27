import math


def strange_partition(nums, x):
    min_bound = int(math.ceil(sum(nums) * 1.0 / x))
    max_bound = sum(int(math.ceil(num * 1.0 / x)) for num in nums)
    return min_bound, max_bound


if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        n, x = [int(i) for i in input().split()]
        nums = [int(i) for i in input().split()]
        min_bound, max_bound = strange_partition(nums, x)
        print(min_bound, max_bound)

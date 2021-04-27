def apollo_versus_pan(nums):
    len_num = len(nums)
    bit_set = [sum(1 if num & (1 << i) else 0 for num in nums) for i in range(61)]
    total = 0
    for num in nums:
        sum_and = 0
        sum_or = 0
        for i in range(0, 61):
            if num & (1 << i):
                sum_and += bit_set[i] * (1 << i)
                sum_or += len_num * (1 << i)
            else:
                sum_or += bit_set[i] * (1 << i)
        total += sum_and * sum_or
    return total % (10 ** 9 + 7)


if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        num_num = int(input())
        nums = [int(i) for i in input().split()]
        print(apollo_versus_pan(nums))

# def long_jumps(nums):
#     n = len(nums)
#     visited = [False] * n
#     max_score = 0
#     for i in range(n):
#         if visited[i]:
#             continue
#         j = i
#         while j < n:
#             visited[j] = True
#             j += nums[j]
#         score = j - i
#         if max_score < score:
#             max_score = score
#     return max_score


def long_jumps(nums):
    n = len(nums)
    scores = [0] * n
    max_score = 0
    for i in range(n - 1, -1, -1):
        num = nums[i]
        if i + num >= n:
            score = num
        else:
            score = num + scores[i + num]
        scores[i] = score
        if max_score < score:
            max_score = score
    return max_score


if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        num_num = int(input())
        nums = [int(i) for i in input().split()]
        print(long_jumps(nums))
def even_odd_game(nums):
    nums = sorted(nums, reverse=True)
    alice_score = sum(i if i % 2 == 0 else 0 for i in nums[::2])
    bob_score = sum(i if i % 2 == 1 else 0 for i in nums[1::2])
    if alice_score > bob_score:
        return "Alice"
    elif alice_score == bob_score:
        return "Tie"
    return "Bob"


if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        num_num = int(input())
        nums = [int(i) for i in input().split()]
        print(even_odd_game(nums))

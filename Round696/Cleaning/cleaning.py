def check_piles(piles):
    left = 0
    for pile in piles:
        left = pile - left
        if left < 0:
            return False
    if left != 0:
        return False
    return True


def cleaning(piles):
    difference = sum(piles[::2]) - sum(piles[1::2])
    if difference % 2 != 0:
        return False
    else:
        difference = difference // 2
    if difference == 0:
        if check_piles(piles):
            return True
        for i in range(0, len(piles), 2):
            for j in range(i + 2, len(piles), 2):
                new_piles = list(piles)
                new_piles[i], new_piles[j] = new_piles[j], new_piles[i]
                if check_piles(new_piles):
                    return True
        for i in range(1, len(piles), 2):
            for j in range(i + 2, len(piles), 2):
                new_piles = list(piles)
                new_piles[i], new_piles[j] = new_piles[j], new_piles[i]
                if check_piles(new_piles):
                    return True

    else:
        for i in range(0, len(piles), 2):
            for j in range(1, len(piles), 2):
                if piles[i] - piles[j] == difference:
                    new_piles = list(piles)
                    new_piles[i], new_piles[j] = new_piles[j], new_piles[i]
                    if check_piles(new_piles):
                        return True
    return False


if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        n = [int(i) for i in input().split()]
        piles = [int(i) for i in input().split()]
        if cleaning(piles):
            print("YES")
        else:
            print("NO")

def bovine_dilemma(trees):
    areas = set()
    for i in range(len(trees)):
        for j in range(i + 1, len(trees)):
            areas.add(trees[j] - trees[i])
    return len(areas)


if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        num_tree = int(input())
        trees = [int(i) for i in input().split()]
        print(bovine_dilemma(trees))
def correct_placement(pairs):
    sorted_pairs = [i[0] for i in sorted(enumerate(pairs), key=lambda x: x[1])]
    advantage_pairs = set()
    only_pairs = set()
    placement = [-1] * len(pairs)
    for j in range(len(sorted_pairs)):
        index = sorted_pairs[j]
        pair = pairs[index]
        for advantage_pair in advantage_pairs:
            if pair[0] > advantage_pair[1][0] and pair[1] > advantage_pair[1][1]:
                placement[index] = advantage_pair[0] + 1
                break
            elif pair[0] == advantage_pair[1][0] and pair[1] == advantage_pair[1][1]:
                placement[index] = placement[advantage_pair[0]]
                break
        if placement[index] < 0 and pair not in only_pairs:
            only_pairs.add(pair)
            advantage_pairs.add((index, pair))
    return placement


if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        num_num = int(input())
        pairs = []
        for i in range(num_num):
            pair = tuple(sorted([int(i) for i in input().split()]))
            pairs.append(pair)
        print(" ".join([str(i) for i in correct_placement(pairs)]))

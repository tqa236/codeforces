from bisect import bisect_left
from fractions import Fraction
from tqdm import tqdm
from bisect import bisect_left


def binary_search(a, x):
    pos = bisect_left(a, x)
    return pos if pos != len(a) and a[pos] == x else -1


def two_sum(a, b, target, ms_dict):
    min_val = float("inf")
    for index, num in enumerate(b):
        val = take_closest(a, target - num)
        if abs(target - val - num) < min_val:
            min_val = abs(target - val - num)
            min_index = (ms_dict[val] + 1, index + 1)
    return min_index


def take_closest(myList, myNumber):
    """
    Assumes myList is sorted. Returns closest value to myNumber.

    If two numbers are equally close, return the smallest number.
    """
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
        return after
    else:
        return before


def read_input(file_name):
    inputs = []
    with open(file_name, "r") as f:
        N = int(f.readline().strip())
        for i in range(N):
            m, k, n = [int(i) for i in f.readline().strip().split()]
            # ms = [Fraction(i) for i in f.readline().strip().split()]
            # ks = [Fraction(i) for i in f.readline().strip().split()]
            # ss = [Fraction(i) for i in f.readline().strip().split()]
            ms = [int(Fraction(i) * 10 ** 6) for i in f.readline().strip().split()]
            ks = [int(Fraction(i) * 10 ** 6) for i in f.readline().strip().split()]
            ss = [int(Fraction(i) * 10 ** 6) for i in f.readline().strip().split()]
            inputs.append((ms, ks, ss))
    return N, inputs


def solve(file_name):
    print("Read input")
    N, inputs = read_input(file_name)
    for test, values in enumerate(inputs):
        if test < 1:
            continue
        print("Test", test)
        results = []
        ms, ks, ss = values
        sorted_ms = sorted(ms)
        ms_dict = {val: key for key, val in enumerate(ms)}
        results = []
        for s in tqdm(ss):
            results.append(two_sum(sorted_ms, ks, s, ms_dict))
        write_output(file_name, results, test)


def write_output(file_name, finals, testcase=None):
    output_name = f"output3_{file_name}"

    with open(output_name, "a") as f:
        if testcase is not None:
            for val in finals:
                f.writelines(" ".join(map(str, val)) + "\n")
        else:
            for test, final in enumerate(finals):
                for val in final:
                    f.writelines(" ".join(map(str, val)) + "\n")


if __name__ == "__main__":
    # for i in range(5, 6):
    #     solve(f"{i}.txt")
    solve(f"3.txt")
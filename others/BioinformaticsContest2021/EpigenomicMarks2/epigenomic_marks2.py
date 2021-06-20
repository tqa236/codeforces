import numpy as np


def read_input(file_name):
    results = []
    with open(file_name, "r") as f:
        N = int(f.readline().strip())
        for i in range(N):
            n, l = [int(i) for i in f.readline().strip().split()]
            result = []
            for i in range(n):
                array = [int(i) for i in f.readline().strip()]
                result.append(array)
            results.append(result)
    return N, results


def solve(file_name):
    finals = []
    N, results = read_input(file_name)
    for result in results:
        array = np.array(result)
        unique_cols, indices = np.unique(array, axis=1, return_inverse=True)
        indices = indices + 1
        finals.append(indices)
    write_output(file_name, finals)


def write_output(file_name, finals):
    output_name = f"output_{file_name}"

    with open(output_name, "w") as f:
        for final in finals:
            n = len(set(final))
            f.writelines(str(n) + "\n")
            f.writelines(" ".join(map(str, final)) + "\n")


if __name__ == "__main__":
    solve("1.txt")
    solve("2.txt")
    solve("sample.txt")

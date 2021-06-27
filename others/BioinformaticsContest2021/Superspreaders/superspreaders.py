import numpy as np
from fractions import Fraction
import random
import statistics
from tqdm import tqdm


def read_input(file_name):
    results = []
    Vs = []
    with open(file_name, "r") as f:
        T = int(f.readline().strip())
        for i in range(T):
            V, D = [int(i) for i in f.readline().strip().split()]
            Vs.append(V)
            result = []
            for i in range(D):
                num_contacts = int(f.readline().strip())
                array = []
                for j in range(num_contacts):
                    tmp = f.readline().strip().split()
                    a, b, p = int(tmp[0]), int(tmp[1]), Fraction(tmp[2])
                    array.append((a, b, p))
                result.append(array)
            results.append(result)
    return T, Vs, results


def solve(file_name):
    T, Vs, contacts = read_input(file_name)
    finals = []
    attempt = 1
    for i in tqdm(range(T)):
        V = Vs[i]
        contact = contacts[i]
        results = []
        # print(contact)
        # print(len(contact))
        for j in range(1, V + 1):
            result = []
            for k in range(attempt):
                people = [False] * V
                people[j - 1] = True
                for l in range(7):
                    new = []
                    for close in contact[l]:
                        # print(close)
                        if people[close[0] - 1] and not people[close[1] - 1]:
                            random_number = random.SystemRandom().random()
                            if close[2] >= random_number:
                                new.append(close[1])
                    for val in new:
                        people[val - 1] = True
                result.append(sum(people))
            results.append(statistics.median(result))
        # print(results)
        finals.append(results.index(max(results)) + 1)
    print(finals)
    write_output(file_name, finals)


def write_output(file_name, finals):
    output_name = f"output_{file_name}"

    with open(output_name, "w") as f:
        for final in finals:
            f.writelines(str(final) + "\n")


if __name__ == "__main__":
    solve("test4")

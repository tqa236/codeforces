if __name__ == "__main__":
    with open("input.txt", "r") as f:
        n = int(f.readline())
        result = []
        for i in range(n):
            array = [int(i) for i in f.readline().split()]
            result.append(sum(array))
    with open("output.txt", "w") as f:
        for i in result:
            f.writelines(str(i) + "\n")
import re

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        n = int(f.readline())
        result = []
        for i in range(n):
            s = f.readline().strip()
            t = f.readline().strip()
            array = [m.start() + 1 for m in re.finditer(f"(?={t})", s)]
            result.append(array)
    with open("output.txt", "w") as f:
        for i in result:
            f.writelines(" ".join(map(str, i)) + "\n")
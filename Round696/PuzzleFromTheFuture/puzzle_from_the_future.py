def puzzle_from_the_future(length, b):
    a = ""
    for i in b:
        if not a:
            a += "1"
        else:
            if (last_digit, i) in [
                ("1", "1"),
                ("2", "0"),
                ("0", "0"),
                ("0", "1"),
            ]:
                a += "1"
            else:
                a += "0"
        last_digit = str(int(i) + int(a[-1]))
    return a


if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        length = int(input())
        b = input()
        print(puzzle_from_the_future(length, b))
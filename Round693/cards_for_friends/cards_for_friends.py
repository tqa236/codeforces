def cards_for_friends(w, h, n):
    w2 = 1
    while w % 2 == 0:
        w2 *= 2
        w = w / 2
    h2 = 1
    while h % 2 == 0:
        h2 *= 2
        h = h / 2
    return w2 * h2 >= n


if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        w, h, n = [int(i) for i in input().split()]
        if cards_for_friends(w, h, n):
            print("YES")
        else:
            print("NO")
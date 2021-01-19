def {function}():
    pass

if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        n, m = [int(i) for i in input().split()]
        friends = [int(i) for i in input().split()]
        presents = [int(i) for i in input().split()]
        print({function}(friends, presents))
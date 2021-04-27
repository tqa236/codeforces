def last_minute_enhancements(nodes):
    count = 0
    current_node = 0
    for node in nodes:
        if node > current_node:
            count += 1
            current_node = node
        elif node == current_node:
            count += 1
            current_node = node + 1
    return count


if __name__ == "__main__":
    num_test = int(input())
    for i in range(num_test):
        num_node = int(input())
        nodes = [int(i) for i in input().split()]
        print(last_minute_enhancements(nodes))

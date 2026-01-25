import sys


def func(n, a, adj):
    parent = [0] * (n + 1)
    order = [1]

    queue_ptr = 0
    while queue_ptr < len(order):
        u = order[queue_ptr]
        queue_ptr += 1

        real_children = []
        for v in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            real_children.append(v)
            order.append(v)

        adj[u] = real_children

    can_0 = bytearray(n + 1)
    can_1 = bytearray(n + 1)

    for i in range(n - 1, -1, -1):
        u = order[i]
        val_u = a[u]
        p = parent[u]
        val_p = a[p] if p != 0 else 0

        target_0 = (val_u + val_p + 1) & 1

        target_1 = (val_u + 1) & 1

        current_sum_parity = 0
        can_flip = False
        possible = True

        for v in adj[u]:
            c0 = can_0[v]
            c1 = can_1[v]

            if not c0 and not c1:
                possible = False
                break

            if c0 and c1:
                if a[v] & 1:
                    can_flip = True
            elif c0:
                pass
            else:
                current_sum_parity ^= a[v] & 1

        if not possible:
            continue

        if u != 1:
            if can_flip or current_sum_parity == target_0:
                can_0[u] = 1

        if can_flip or current_sum_parity == target_1:
            can_1[u] = 1

    if not can_1[1]:
        return "NO"

    seq = []

    stack = [(1, 1, False)]

    while stack:
        u, state, processed = stack.pop()

        if processed:
            seq.append(str(u))
            continue

        val_u = a[u]
        p = parent[u]
        val_p = a[p] if p != 0 else 0

        target = 0
        if state == 0:
            target = (val_u + val_p + 1) & 1
        else:
            target = (val_u + 1) & 1

        current_sum_parity = 0
        flip_node = -1

        for v in adj[u]:
            c0 = can_0[v]
            c1 = can_1[v]

            if c0 and c1:
                if a[v] & 1:
                    flip_node = v
            elif c1:
                current_sum_parity ^= a[v] & 1

        do_flip_node = False
        if current_sum_parity != target:
            do_flip_node = True

        group_0 = []
        group_1 = []

        for v in adj[u]:
            c0 = can_0[v]
            c1 = can_1[v]

            chosen_state = 0

            if c0 and c1:
                if v == flip_node and do_flip_node:
                    chosen_state = 1
                else:
                    chosen_state = 0
            elif c0:
                chosen_state = 0
            else:
                chosen_state = 1

            if chosen_state == 1:
                group_1.append(v)
            else:
                group_0.append(v)

        for v in reversed(group_1):
            stack.append((v, 1, False))

        stack.append((u, state, True))

        for v in reversed(group_0):
            stack.append((v, 0, False))

    return "YES\n" + " ".join(seq)


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n = int(parse_input())
        a = [0] + [int(i) for i in parse_input().split()]
        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u, v = [int(i) for i in parse_input().split()]
            adj[u].append(v)
            adj[v].append(u)
        result.append(func(n, a, adj))
    print("\n".join(map(str, result)))


parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

if __name__ == "__main__":
    main()

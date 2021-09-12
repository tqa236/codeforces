#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter
import queue

sys.setrecursionlimit(10 ** 9)


class TreeNode:
    def __init__(self, index, parent):
        self.index = index
        self.parent = parent
        self.edges = []
        self.children = []


# def func(n, nodes):
#     leaves = [False] * n
#     buds = [False] * n
#     false_buds = [False] * n
#     in_queue = [False] * n
#     in_queue[0] = True

#     queue_nodes = [0]
#     while queue_nodes:
#         node_index = queue_nodes.pop()
#         node = nodes[node_index]
#         if not node.children and node.parent != 0:
#             leaves[node_index] = True
#         for child_index in node.children:
#             queue_nodes.append(child_index)

#     queue_nodes = [0]

#     while queue_nodes:
#         node_index = queue_nodes.pop()
#         node = nodes[node_index]
#         if node.children:
#             is_bud = True
#             is_false_bud = False
#             for child_index in node.children:
#                 queue_nodes.append(child_index)
#                 if not leaves[child_index]:
#                     is_bud = False
#                 else:
#                     is_false_bud = True
#             if node_index != 0:
#                 if is_bud:
#                     buds[node_index] = True
#                 elif is_false_bud:
#                     false_buds[node_index] = True
#     # print(leaves)
#     # print(buds)
#     # print(false_buds)
#     return sum(leaves) - sum(buds) - sum(false_buds) + 1


def func(n, nodes):
    leaves = [False] * n
    buds = [False] * n
    false_buds = [False] * n

    in_queue = [False] * n
    in_queue[0] = True

    queue_nodes = [0]
    while queue_nodes:
        node_index = queue_nodes.pop()
        node = nodes[node_index]
        if not node.children:
            # if not node.children and node.parent != 0:
            leaves[node_index] = True
        for child_index in node.children:
            queue_nodes.append(child_index)

    no_branch_bool = [False] * n
    no_branches = [i for i in range(n) if leaves[i] and nodes[i].parent != 0]
    c = 0
    f = False
    for leave_index in no_branches:
        node_index = leave_index
        while len(nodes[nodes[node_index].parent].children) == 1:
            f = True
            no_branch_bool[node_index] = True
            node_index = nodes[node_index].parent
            no_branch_bool[node_index] = True
        if f:
            c += 1
        f = False
    # print(no_branch_bool)
    # print(leaves)
    # print([i for i in nodes[0].children if leaves[i]])
    return len([i for i in range(n) if leaves[i] and not no_branch_bool[i]]) - min(
        0, len([i for i in nodes[0].children if leaves[i]]) - c
    )
    print(no_branch_bool)
    count = 0

    queue_nodes = [0]
    while queue_nodes:
        node_index = queue_nodes.pop()
        node = nodes[node_index]
        print(node_index, queue_nodes)
        if not no_branch_bool[node_index]:
            print("Inside")
            if not node.children and node.parent != 0:
                count += 1
            for child_index in node.children:
                queue_nodes.append(child_index)
    return count
    # print(leaves)
    # print(buds)
    # print(false_buds)
    return sum(leaves) - sum(buds) - sum(false_buds) + 1


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n = int(parse_input())
        nodes = [TreeNode(i, None) for i in range(n)]
        for j in range(n - 1):
            u, v = [int(i) - 1 for i in parse_input().split()]
            nodes[u].edges.append(v)
            nodes[v].edges.append(u)
        queue_nodes = [0]
        in_queue = [False] * n
        in_queue[0] = True
        while queue_nodes:
            node_index = queue_nodes.pop()
            node = nodes[node_index]
            for edge_index in node.edges:
                if edge_index != node.parent:
                    nodes[edge_index].parent = node_index
                    queue_nodes.append(edge_index)
                    node.children.append(edge_index)
        result.append(func(n, nodes))
    print("\n".join(map(str, result)))


# region fastio

# BUFSIZE = 8192


# class FastIO(IOBase):
#     newlines = 0

#     def __init__(self, file):
#         self._fd = file.fileno()
#         self.buffer = BytesIO()
#         self.writable = "x" in file.mode or "r" not in file.mode
#         self.write = self.buffer.write if self.writable else None

#     def read(self):
#         while True:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             if not b:
#                 break
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines = 0
#         return self.buffer.read()

#     def readline(self):
#         while self.newlines == 0:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             self.newlines = b.count(b"\n") + (not b)
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines -= 1
#         return self.buffer.readline()

#     def flush(self):
#         if self.writable:
#             os.write(self._fd, self.buffer.getvalue())
#             self.buffer.truncate(0), self.buffer.seek(0)


# class IOWrapper(IOBase):
#     def __init__(self, file):
#         self.buffer = FastIO(file)
#         self.flush = self.buffer.flush
#         self.writable = self.buffer.writable
#         self.write = lambda s: self.buffer.write(s.encode("ascii"))
#         self.read = lambda: self.buffer.read().decode("ascii")
#         self.readline = lambda: self.buffer.readline().decode("ascii")


# sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()

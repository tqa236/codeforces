#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


class TreeNode:
    def __init__(self, val_left, val_right, left=None, right=None):
        self.val_left = val_left
        self.val_right = val_right
        self.left = left
        self.right = right


def make_tree(values):
    """Make a tree from a list using BFS."""
    if not values:
        return None
    root = TreeNode(values[0][0], values[0][1], None, None)
    nodes = []
    queue = [root]
    for index, value in enumerate(values[1:]):
        node = queue[0]
        if index % 2 == 0:
            if value is not None:
                node.left = TreeNode(value, None, None)
                queue.append(node.left)
        else:
            if value is not None:
                node.right = TreeNode(value, None, None)
                queue.append(node.right)
            queue.pop(0)
    return root


def func(n, nodes, edges):
    pass


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n = int(parse_input())
        nodes = []
        for i in range(n):
            array = [int(i) for i in parse_input().split()]
            nodes.append(array)
        edges = []
        for i in range(n - 1):
            array = [int(i) for i in parse_input().split()]
            edges.append(array)
        result.append(func(n, nodes, edges))
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

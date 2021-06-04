#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


class TreeNode:
    def __init__(self, index, val, left=None, right=None):
        self.index = index
        self.val = val
        self.left = left
        self.right = right


def func(round, result, num_query, queries):
    nodes = []
    last_round_game = 0
    for i, val in enumerate(result):
        # print(i, val, last_round_game, len(nodes))
        if i < 2 ** (round - 1):
            value = 1 if val is not None else 2
            node = TreeNode(i, value)
            nodes.append(node)
        else:
            left = nodes[last_round_game]
            right = nodes[last_round_game + 1]
            if val is None:
                value = left.val + right.val
            elif val == 0:
                value = left.val
            else:
                value = right.val
            node = TreeNode(i, value, left, right)
            nodes.append(node)
            last_round_game += 2
    sequence = []
    for match, val in queries:
        print("query", match, val)
        node = nodes[match - 1]
        if node.left is not None:
            if val is None:
                value = node.left.val + node.right.val
            elif val == 0:
                value = node.left.val
            else:
                value = node.right.val
        else:
            if val is None:
                value = 2
            else:
                value = 1
        diff = value - node.val
        offset = 2 ** round - match
        sequence = []
        while offset > 1:
            # print(offset)
            if offset % 2 == 0:
                res = "right"
            else:
                res = "left"
            tmp = offset // 2
            node = nodes[2 ** round - tmp - 1]
            if res == "left" and node.val == 1 or res == "right" and node.val == 0:
                print("break")
                break
            offset = offset // 2
        print("diff", diff)
        # print("Offset", offset)
        if offset == 1:
            print(nodes[-1].val + diff)
        else:
            print(nodes[-1].val)
        # while node.index != 2 ** round - 1:


def main():
    round = int(parse_input())
    result = [int(i) if i != "?" else None for i in parse_input()]
    num_query = int(parse_input())
    queries = []
    for _ in range(num_query):
        array = [int(i) if i != "?" else None for i in parse_input().split()]
        queries.append(array)
    func(round, result, num_query, queries)


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

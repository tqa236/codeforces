#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter
import operator


def func(n, array):
    while 0 in array:
        array = [i - 1 for i in array]
        # if 0 not in array:
        #     break
    find = None
    nodes = {}
    for i, val in enumerate(array):
        if val > 0:
            nodes[i] = val
    if not nodes:
        print(f"! 0 0")
        sys.stdout.flush()
        return
    sorted_nodes = sorted(nodes.items(), key=operator.itemgetter(1))
    # print(sorted_nodes)
    i = 0
    j = len(sorted_nodes) - 1
    while j > i:
        print(f"? {sorted_nodes[i][0]+1} {sorted_nodes[j][0]+1}")
        sys.stdout.flush()
        result = parse_input()
        if result == "Yes":
            print(f"! {sorted_nodes[i][0]+1} {sorted_nodes[j][0]+1}")
            sys.stdout.flush()
            return
        if (
            sorted_nodes[i + 1][1] - sorted_nodes[i][1]
            == sorted_nodes[j][1] - sorted_nodes[j - 1][1]
        ):
            if j - i > 1:
                print(f"? {sorted_nodes[i+1][0]+1} {sorted_nodes[j][0]+1}")
                sys.stdout.flush()
                result = parse_input()
                if result == "Yes":
                    print(f"! {sorted_nodes[i+1][0]+1} {sorted_nodes[j][0]+1}")
                    sys.stdout.flush()
                    return
                print(f"? {sorted_nodes[i][0]+1} {sorted_nodes[j-1][0]+1}")
                sys.stdout.flush()
                result = parse_input()
                if result == "Yes":
                    print(f"! {sorted_nodes[i][0]+1} {sorted_nodes[j-1][0]+1}")
                    sys.stdout.flush()
                    return
            i += 1
            j -= 1
        elif (
            sorted_nodes[i + 1][1] - sorted_nodes[i][1]
            < sorted_nodes[j][1] - sorted_nodes[j - 1][1]
        ):
            i += 1
        else:
            j -= 1
    print("! 0 0")
    sys.stdout.flush()
    # for key, val in sorted_diff:
    #     print(f"{key[0]} {key[1]}")


def main():
    n = int(parse_input())
    array = [int(i) for i in parse_input().split()]
    func(n, array)


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
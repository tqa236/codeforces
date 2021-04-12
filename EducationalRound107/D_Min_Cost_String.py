#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter
import string

PATH = []


def printCircuit(adj):

    # adj represents the adjacency list of
    # the directed graph

    if len(adj) == 0:
        return  # empty graph

    # Maintain a stack to keep vertices
    # We can start from any vertex, here we start with 0
    curr_path = [0]

    # list to store final circuit
    circuit = []

    while curr_path:

        curr_v = curr_path[-1]

        # If there's remaining edge in adjacency list
        # of the current vertex
        if adj[curr_v]:

            # Find and remove the next vertex that is
            # adjacent to the current vertex
            next_v = adj[curr_v].pop()

            # Push the new vertex to the stack
            curr_path.append(next_v)

        # back-track to find remaining circuit
        else:
            # Remove the current vertex and
            # put it in the curcuit
            circuit.append(curr_path.pop())

    # we've got the circuit, now print it in reverse
    for i in range(len(circuit) - 1, -1, -1):
        PATH.append(circuit[i])


def func(n, k):
    adj1 = [list(range(k)) for i in range(k)]
    printCircuit(adj1)
    base = [string.ascii_lowercase[i] for i in PATH[:-1]]
    return "".join(base * (n // len(base) + 1))[:n]


def main():
    n, k = [int(i) for i in parse_input().split()]
    print(func(n, k))


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
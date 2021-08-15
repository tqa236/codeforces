#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter

M1_ROOT_CACHES = {}
M2_ROOT_CACHES = {}


def update_node(node, val, edges, root_caches):
    while True:
        tmp = edges[node]
        edges[node] = find_root(val, edges, root_caches)
        if node == edges[node]:
            break
        node = tmp


def find_root(node, edges, root_caches):
    org_node = node
    node = root_caches[node]
    while node != edges[node]:
        node = edges[node]
    root_caches[org_node] = node
    return node


def func(n, m1_edges, m2_edges):
    result = []
    # print(m1_edges, m2_edges)
    for i in range(1, n + 1):
        val1 = find_root(i, m1_edges, M1_ROOT_CACHES)
        val3 = find_root(i, m2_edges, M2_ROOT_CACHES)
        for j in range(i + 1, n + 1):
            val2 = find_root(j, m1_edges, M1_ROOT_CACHES)
            val4 = find_root(j, m2_edges, M2_ROOT_CACHES)
            # print(i, j, val1, val2, val3, val4)
            if val1 != val2 and val3 != val4:
                result.append([i, j])
                if val1 > val2:
                    update_node(i, j, m1_edges, M1_ROOT_CACHES)
                    val1 = find_root(i, m1_edges, M1_ROOT_CACHES)
                else:
                    update_node(j, i, m1_edges, M1_ROOT_CACHES)
                if val3 > val4:
                    update_node(i, j, m2_edges, M2_ROOT_CACHES)
                    val3 = find_root(i, m2_edges, M2_ROOT_CACHES)
                else:
                    update_node(j, i, m2_edges, M2_ROOT_CACHES)
                # print(i, j, m1_edges, m2_edges)
    print(len(result))
    for val in result:
        print(val[0], val[1])


def main():
    n, m1, m2 = [int(i) for i in parse_input().split()]
    m1_edges = {}
    for i in range(1, n + 1):
        m1_edges[i] = i
        M1_ROOT_CACHES[i] = i
    m2_edges = {}
    for i in range(1, n + 1):
        m2_edges[i] = i
        M2_ROOT_CACHES[i] = i
    for i in range(m1):
        array = [int(i) for i in parse_input().split()]
        if m1_edges[array[1]] > m1_edges[array[0]]:
            update_node(array[1], array[0], m1_edges, M1_ROOT_CACHES)
        elif m1_edges[array[1]] < m1_edges[array[0]]:
            update_node(array[0], array[1], m1_edges, M1_ROOT_CACHES)
    for i in range(m2):
        array = [int(i) for i in parse_input().split()]
        if m2_edges[array[1]] > m2_edges[array[0]]:
            update_node(array[1], array[0], m2_edges, M2_ROOT_CACHES)
        elif m2_edges[array[1]] < m2_edges[array[0]]:
            update_node(array[0], array[1], m2_edges, M2_ROOT_CACHES)
    func(n, m1_edges, m2_edges)


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()

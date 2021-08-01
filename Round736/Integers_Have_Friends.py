#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter
import operator


def printDivisors(n):
    all_div = set()
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            if n == i * i:
                all_div.add(i)
            else:
                all_div.add(i)
                all_div.add(n // i)
        i = i + 1
    return all_div


def func(n, array):

    if n == 1:
        return 1
    result_max = {}
    result = {}
    for i in range(n - 1):
        divisors = printDivisors(abs(array[i + 1] - array[i]))
        for val in divisors:
            if (val, array[i] % val) not in result:
                result[(val, array[i] % val)] = (i, i + 1)
            else:
                if result[(val, array[i] % val)][1] != i:
                    if (val, array[i] % val) not in result_max:
                        result_max[(val, array[i] % val)] = (
                            result[(val, array[i] % val)][1]
                            - result[(val, array[i] % val)][0]
                            + 1
                        )
                    else:
                        result_max[(val, array[i] % val)] = max(
                            result_max[(val, array[i] % val)],
                            (
                                result[(val, array[i] % val)][1]
                                - result[(val, array[i] % val)][0]
                                + 1
                            ),
                        )
                    del result[(val, array[i] % val)]
                else:
                    result[(val, array[i] % val)] = (
                        result[(val, array[i] % val)][0],
                        i + 1,
                    )
    # print(result)
    for key, val in result.items():
        if key not in result_max:
            result_max[key] = val[1] - val[0] + 1
        else:
            result_max[key] = max(result_max[key], val[1] - val[0] + 1)
            # print(printDivisors(abs(array[j] - array[i])))
    # print(result)
    # print(result)
    max_val = -1
    for key, val in result_max.items():
        if key[0] != 1:
            max_val = max(max_val, val)
    return max_val


def main():
    num_test = int(parse_input())
    result = []
    for _ in range(num_test):
        n = int(parse_input())
        array = [int(i) for i in parse_input().split()]
        result.append(func(n, array))
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

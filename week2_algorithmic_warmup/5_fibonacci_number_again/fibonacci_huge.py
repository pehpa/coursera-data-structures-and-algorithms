import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+"/../..")
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+"/../1_fibonacci_number")
from fibonacci import fib_fast_doubling


def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


# def fib_fast_doubling(n):
#     if n < 0:
#         raise ValueError("Negative arguments not implemented")
#     return _fib(n)[0]


# def _fib(n):
#     if n == 0:
#         return (0, 1)
#     else:
#         a, b = _fib(n // 2)
#         c = a * (b * 2 - a)
#         d = a * a + b * b
#         if n % 2 == 0:
#             return (c, d)
#         else:
#             return (d, c + d)


def pisano(m):
    prev = 0
    curr = 1
    res = 0

    for i in range(m * m):
        prev, curr = curr, (prev + curr) % m

        if prev == 0 and curr == 1:
            res = i + 1
    return res


def fibonacci_huge_pisano(n, m):
    # get reduced fibonacci by using the pisano number
    f = n % pisano(m)

    # return the fth fibonacci number modulo m
    return fib_fast_doubling(f) % m


if __name__ == '__main__':
    n, m = map(int, input().split())
    # print(fibonacci_huge_naive(n, m))
    print(fibonacci_huge_pisano(n, m))

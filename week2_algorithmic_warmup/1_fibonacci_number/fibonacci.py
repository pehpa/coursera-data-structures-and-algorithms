import time
import random
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+"/../..")
from utils.stress_test import stress_test

DO_STRESS_TEST = False


def fibonacci_number(n):
    if n <= 1:
        return n

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)


def fib_fast_doubling(n):
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return _fib(n)[0]


def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)


if __name__ == '__main__':
    if DO_STRESS_TEST:
        stress_test(fib_fast_doubling, 1)
    else:
        input_n = int(input())
        print(fib_fast_doubling(input_n))

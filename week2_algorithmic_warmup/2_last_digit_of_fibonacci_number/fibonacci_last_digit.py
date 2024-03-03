import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+"/../..")
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+"/../1_fibonacci_number")
from fibonacci import fib_fast_doubling


def fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def last_digit(n):
    return fib_fast_doubling(n) % 10


if __name__ == '__main__':
    n = int(input())
    print(last_digit(n))

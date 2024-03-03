import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../..")
from utils.stress_test import stress_test

DO_STRESS_TEST = False


def fibonacci_sum(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10


def fibonacci_sum_fast(n):
    # Assumptions:
    # 1. Fn mod 10 gives the remainder of the nth Fibonacci number
    # 2. the Pisano period mod 10 repeats every 60 numbers
    # 3. thus just sum up the Pisano period and modulo 10 to get the last digit
    # 4. use knowledge that sum(n) = F(n+2) - 1
    if n < 2:
        return n

    prev, curr, sum = 0, 1, -1
    limit = n % 60  # pisano_length(10) = 60

    for i in range(0, limit+1):
        prev, curr = curr, (prev + curr) % 10

    sum = curr - 1 if curr != 0 else 9
    return sum


if __name__ == '__main__':
    if DO_STRESS_TEST:
        stress_test(fibonacci_sum_fast, 1, max_n=100000000000000000000000)
    else:
        n = int(input())
        # print(fibonacci_sum(n))
        print(fibonacci_sum_fast(n))

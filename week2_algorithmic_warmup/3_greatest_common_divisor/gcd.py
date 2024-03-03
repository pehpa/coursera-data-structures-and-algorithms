import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../..")
from utils.stress_test import stress_test

DO_STRESS_TEST = False


def gcd(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_fast_2(a, b):
    """Recursive implementation of Euclid's algorithm. Assumes a >= 1 and b >= 0 and a >= b.

    Args:
        a (int): integer >= 1
        b (int): integer >= 0

    Returns:
        int: greatest common divisior, integer >= 1
    """
    assert (a >= b) and (a > 0) and (b >= 0)
    if b == 0:
        return a
    else:
        a_dash = a % b
        return gcd_fast_2(b, a_dash)


def gcd_fast_2_init(a, b):
    return gcd_fast_2(max(a, b), min(a, b))


if __name__ == "__main__":
    if DO_STRESS_TEST:
        stress_test(gcd_fast_2_init, 2, max_n=10000000)
    else:
        a, b = map(int, input().split())
        print(gcd_fast_2_init(a, b))

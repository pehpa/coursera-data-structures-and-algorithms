import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../..")
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/../3_greatest_common_divisor")
from gcd import gcd_fast


def lcm(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    assert False


def lcm_fast(a, b):
    return int(a * b / gcd_fast(a, b))


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_fast(a, b))

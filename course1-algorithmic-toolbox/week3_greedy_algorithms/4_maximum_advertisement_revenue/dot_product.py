from itertools import permutations


def max_dot_product(first_sequence, second_sequence):
    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(first_sequence[i] * permutation[i]
                          for i in range(len(first_sequence)))
        max_product = max(max_product, dot_product)

    return max_product


def max_prod(first_sequence, second_sequence):
    res = 0
    for a, b in zip(sorted(first_sequence), sorted(second_sequence)):
        res = res + (a * b)
    return res


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n

    # result: 230 = 30 * 5 + 20 * 3 + 10 * 2
    # n = 3
    # prices = [2, 3, 5]
    # clicks = [10, 20, 30]

    # result: 897 = 23·39
    # n = 1
    # prices = [23]
    # clicks = [39]

    # result: 79 = 7·9 + 2·2 + 3·4
    # n = 3
    # prices = [2, 3, 9]
    # clicks = [7, 4, 2]

    # print("n = {}, clicks = {}, prices = {}".format(n, clicks, prices))

    # print(max_dot_product(prices, clicks))
    print(max_prod(prices, clicks))

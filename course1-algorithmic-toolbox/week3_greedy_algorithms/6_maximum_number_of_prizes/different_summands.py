import math

def optimal_summands(n):
    summands = []

    m = 1
    r = n - 1
    
    while m < r:
        summands.append(m)
        # print("while: m={}, summands={}, r={}".format(m, summands, r))
        m = m + 1
        r = r - m
    summands.append(r + m)
    # print("summands = {}, sum = {}".format(summands, sum(summands)))

    return summands

def analytic_solution(n):
    # compute maximum number so that summands = 1 + 2 + 3 + ... + max_n + r
    # where r = n - sum(1 + 2 + 3 + ... + max_n)
    max_n = (-3. + math.sqrt(9. + 8. * n)) / 2.
    if math.floor(max_n) == max_n:
        max_n = int(max_n) - 1
    else:
        max_n = int(max_n)

    summands = list(range(1, max_n + 1))
    summands.append(n - sum(summands))

    return summands


if __name__ == '__main__':
    n = int(input())

    # n = 6  # result: 3 / 1 2 3
    # n = 8  # result: 3 / 1 2 5
    # n = 2  # result: 1 / 2

    # summands = optimal_summands(n)
    summands = analytic_solution(n)

    print(len(summands))
    print(*summands)

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


if __name__ == '__main__':
    n = int(input())

    # n = 6  # result: 3 / 1 2 3
    # n = 8  # result: 3 / 1 2 5
    # n = 2  # result: 1 / 2
    # n = 454351

    summands = optimal_summands(n)

    print(len(summands))
    print(*summands)

from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    values_per_weights = [a/b for a, b in zip(values, weights)]
    # print(values_per_weights)

    for curr_vpw, curr_value, curr_weight in [(vpw, v, w) for vpw, v, w in sorted(zip(values_per_weights, values, weights), reverse=True)]:
        taken_weight = min(capacity, curr_weight)
        taken_value = taken_weight * curr_vpw
        # print('curr value = {:>3}, weight = {:>2}, value/weight = {} | capa bef = {:>2}, val before = {:5.1f}, val taken = {:>2}, weight taken = {:5.1f} | '
        #       .format(curr_value, curr_weight, curr_vpw, capacity, value, taken_weight, taken_value), end='')
        value = value + taken_value
        capacity = capacity - taken_weight
        # print('capa after = {:>2}, overall value = {:4.1f}'.format(capacity, value))

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    # data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    
    # n, capacity = 3, 50
    # values = [60, 100, 120]
    # weights = [20, 50, 30]

    # n, capacity = 1, 10
    # values = [500]
    # weights = [30]

    # print(n, capacity, weights, values)

    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

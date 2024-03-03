
def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10


def fibonacci_partial_sum_fast(from_, to):
    assert from_ <= to  # from the assumptions in the problem statement
    
    m = from_ % 60  # pisano_length(10) = 60
    n = to % 60  # pisano_length(10) = 60

    # if n is smaller than m, add one more pisano period to n
    if n < m:
        n += 60

    curr, next, sum = 0, 1, 0

    for i in range(n + 1):
        if i >= m:
            sum += curr
        curr, next = next, next + curr

    return sum % 10


if __name__ == '__main__':
    # input = sys.stdin.read();
    # from_, to = map(int, input.split())
    from_, to = map(int, input().split())
    # print(fibonacci_partial_sum_naive(from_, to))
    # from_, to = 5618252, 6583591534156
    # from_, to = 10, 10
    print(fibonacci_partial_sum_fast(from_, to))

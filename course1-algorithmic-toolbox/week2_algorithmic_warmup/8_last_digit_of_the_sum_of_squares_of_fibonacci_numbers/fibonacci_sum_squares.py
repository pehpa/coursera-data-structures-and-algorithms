
def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    previous, current, sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def fibonacci_sum_squares_fast(n):
    # uses F0^2 + F1^2 + ... + Fn^2 = Fn + Fn+1
    curr, next = 0, 1

    for i in range(n % 60):
        curr, next = next, (curr + next) % 10

    return (curr * next) % 10


if __name__ == '__main__':
    n = int(input())
    # print(fibonacci_sum_squares(n))
    print(fibonacci_sum_squares_fast(n))

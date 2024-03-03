def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_product_fast(numbers):
    max_num_1 = max(numbers)    
    max_num_1_idx = numbers.index(max_num_1)
    max_num_2 = max(numbers[:max_num_1_idx] + numbers[max_num_1_idx+1:])
    return max_num_1 * max_num_2

def max_pairwise_product_fast2(numbers):
    numbers.sort(reverse=True)
    return numbers[0] * numbers[1]

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product_fast2(input_numbers))

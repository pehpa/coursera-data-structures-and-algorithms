from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    # implements bubble sort
    sorted_list = [numbers.pop(0)]
    while len(numbers) > 0:
        next_num = numbers.pop(0)
        target_idx = 0

        while target_idx < len(sorted_list) and int(str(next_num)+str(sorted_list[target_idx])) < int(str(sorted_list[target_idx])+str(next_num)):
            target_idx = target_idx + 1
        sorted_list.insert(target_idx, next_num)

    # create joint number
    largest_number = ''
    for n in sorted_list:
        largest_number = largest_number + str(n)

    return int(largest_number)


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()

    # input_numbers = [21, 2]  # 2 21
    # input_numbers = [9, 4, 6, 1, 9]  # 9 9 6 4 1
    # input_numbers = [23, 39, 92]  # 92 39 23
    # input_numbers = [2, 3, 9]  # 9 3 2
    # input_numbers = [6, 61, 68]  # 68 6 61
    # input_numbers = [4, 42, 46, 427, 465]  # 465 46 4 427 42
    # input_numbers = [5, 52, 57, 517, 532, 569, 581]  # 581 57 569 5 532 52 517

    # print(largest_number_naive(input_numbers))
    print(largest_number(input_numbers))

from typing import List
from itertools import combinations

from day1 import get_input


def find_number(input: List[int], preamble_index: int, how_many: int):
    for i in range(preamble_index, len(input)):
        comb = combinations(input[i - preamble_index:i], how_many)
        sums = set([x + y for (x, y) in comb])
        if input[i] not in sums:
            return input[i]


def search_for_sum(number: int, input: List[int]):
    how_many_numbers = 2
    while how_many_numbers < len(input):
        for i in range(len(input) - how_many_numbers + 1):
            sublist = input[i:i + how_many_numbers]
            if sum(sublist) == number:
                return sublist
        how_many_numbers += 1
    return None


if __name__ == '__main__':
    input = get_input('input/day9.txt')
    number_not_in_pattern = find_number(input, preamble_index=25, how_many=2)
    print(f'First number not in pattern: {number_not_in_pattern}')
    sublist = search_for_sum(number_not_in_pattern, input)
    maximum = max(sublist)
    minimum = min(sublist)
    print(f'Sum of min and max: {minimum + maximum}')

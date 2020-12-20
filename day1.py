from functools import reduce
from typing import List
from itertools import combinations


def get_input(path: str):
    input = []
    with open(path, "r") as f:
        for line in f.readlines():
            input.append(int(line.strip()))
    return input


def search_for_numbers_that_sums_to(input: List, num: int, how_many: int = 2):
    for c in combinations(input, how_many):
        if sum(c) == num:
            return c


def multiply_iterable(iterable: List):
    return reduce(lambda x, y: x * y, iterable)


if __name__ == '__main__':
    path = 'input/day1.txt'
    input = get_input(path)
    entries = search_for_numbers_that_sums_to(input, 2020, 3)
    print(f'My entries: {entries}')
    result = multiply_iterable(entries)
    print(f'Result: {result}')

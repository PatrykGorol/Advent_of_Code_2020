import collections
import typing
from typing import List, Tuple
from collections import Counter

from day1 import get_input


def count_differences(input: List[int]):
    return Counter([input[i] - input[i - 1] for i in range(1, len(input))])


def extend_input(input: List[int], max_difference: int = 3):
    extended_input = [0, max(input) + max_difference]
    extended_input.extend(input)
    return sorted(extended_input)


def create_combinations_dict(extended_input: List[int]) -> typing.OrderedDict[int, Tuple[int, ...]]:
    combinations_dict = collections.OrderedDict()
    for number in extended_input:
        combinations_dict[number] = tuple(i for i in extended_input if number < i <= number + 3)
    return combinations_dict


# old, recursion not working
# def count_combinations(number: int = 0):
#     # print(number)
#     global combinations_dict
#     if number == list(combinations_dict.items())[-1][0]:
#         return 1
#     return sum(count_combinations(i) for i in combinations_dict[number])

def count_combinations(combinations_dict: List[int]) -> int:
    counter = {combinations_dict[-1][0]: 1}
    for i in combinations_dict[-2::-1]:
        counter[i[0]] = sum(counter[num] for num in i[1])
    return counter[0]


if __name__ == '__main__':
    input = get_input('input/day10.txt')
    extended_input = extend_input(input)
    # print(extended_input)
    counter = count_differences(extended_input)
    print(counter)
    print(f'Counters multiplication: {counter[1] * counter[3]}')
    print()
    combinations_dict = create_combinations_dict(extended_input)
    # print(combinations_dict)
    number_of_combinations = count_combinations(list(combinations_dict.items()))
    print(f'Number of combinations: {number_of_combinations}')

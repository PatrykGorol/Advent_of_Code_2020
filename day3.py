from functools import reduce
from typing import List

trans_table = str.maketrans('.#', '01')


def get_input(path: str):
    input = []
    with open(path, "r") as f:
        for line in f.readlines():
            # input.append(line.strip().replace('.', '0').replace('#', '1'))
            input.append(make_binary(line.strip()))
    return input


def make_binary(line: str):
    return line.translate(trans_table)


def count_trees(input: List[str], column_offset: int, row_offset: int, start_line: int = 0, start_position: int = 0):
    length = len(input[0])
    counter = int(input[start_line][start_position])
    current_position = start_position
    for line_index in range(start_line + row_offset, len(input), row_offset):
        current_position += column_offset
        counter += int(input[line_index][current_position % length])
    return counter


if __name__ == '__main__':
    input = get_input('input/day3.txt')
    counter_3_1 = count_trees(input, column_offset=3, row_offset=1)
    print(f'Liczba drzew przy jednym przejeźdize: {counter_3_1}')
    counter_1_1 = count_trees(input, column_offset=1, row_offset=1)
    counter_5_1 = count_trees(input, column_offset=5, row_offset=1)
    counter_7_1 = count_trees(input, column_offset=7, row_offset=1)
    counter_1_2 = count_trees(input, column_offset=1, row_offset=2)
    print(f'Liczba drzew różnych przejazdów: {counter_1_1}, {counter_3_1}, {counter_5_1}, {counter_7_1}, {counter_1_2}')
    multiplication = reduce(lambda x, y: x * y, [counter_1_1, counter_3_1, counter_5_1, counter_7_1, counter_1_2])
    print(f'Multiplication: {multiplication}')

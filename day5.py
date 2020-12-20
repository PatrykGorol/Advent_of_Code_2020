from typing import List, Tuple

from day2 import get_input

trans_table = str.maketrans('FBLR', '0101')


def get_rows_and_cols(input: List[str], split_index: int = 7) -> List[Tuple[int, int]]:
    coord_list = []
    for i in input:
        row = int(i[:split_index].translate(trans_table), 2)
        col = int(i[split_index:].translate(trans_table), 2)
        coord_list.append((row, col))
    return coord_list


def get_id_list(coord_list: List[Tuple[int, int]]) -> List[int]:
    return [row * 8 + col for (row, col) in coord_list]


def get_missing_seat(id_list: List[int]) -> set:
    min_id = min(id_list)
    max_id = max(id_list)
    return set(range(min_id, max_id + 1)).difference(set(id_list))


if __name__ == '__main__':
    input = get_input('input/day5.txt')
    coord_list = get_rows_and_cols(input)
    seats_id_list = get_id_list(coord_list)
    max_id = max(seats_id_list)
    print(f'Highest seat id: {max_id}')
    missing_id = get_missing_seat(seats_id_list)
    print(f'Missing seat id: {missing_id}')

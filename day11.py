import numpy as np


def get_input(path: str):
    input = []
    with open(path, 'r') as f:
        for line in f.readlines():
            input.append(translate_line(line.strip()))
    return np.array(input)


def translate_line(line: str):
    return [0 if char == "L" else None for char in line]


def change_seats(array: np.array, max_seats_occcupied: int, adjacent: bool):
    new_array = np.copy(array)
    for x in range(len(array)):
        for y in range(len(array[0])):
            if array[x, y] is None:
                continue
            seats_occupied = get_occupied_seats(array, x, y, adjacent)
            if array[x, y] == 0 and seats_occupied == 0:
                new_array[x, y] = 1
            elif array[x, y] == 1 and seats_occupied > max_seats_occcupied:
                new_array[x, y] = 0
    return new_array


def get_occupied_seats(array: np.array, x: int, y: int, adjacent: bool) -> int:
    if adjacent:
        x0, x1, y0, y1 = max(0, x - 1), min(len(array), x + 2), max(0, y - 1), min(len(array[0]), y + 2)
        return np.count_nonzero(array[x0:x1, y0:y1]) - array[x, y]
    counter = 0
    elements = slice_array(array, x, y)

    for e in elements:
        counter += first_visible_seat(e)
    return counter


def slice_array(array, x, y):
    row_max_index = len(array[0]) - 1
    column_max_index = len(array) - 1

    upper_left = array[x - min(x, y):x, y - min(x, y):y].diagonal().tolist()[::-1]
    upper_middle = array[:x, y].tolist()[::-1]
    upper_right = np.diagonal(
        np.fliplr(array[x - min(x, row_max_index - y):x, y + 1:y + 1 + min(x, row_max_index - y)])).tolist()[::-1]
    middle_left = array[x, :y].tolist()[::-1]
    middle_right = array[x, y + 1:].tolist()
    lower_left = np.diagonal(
        np.fliplr(array[x + 1: x + 1 + min(column_max_index - x, y), y - min(column_max_index - x, y):y])).tolist()
    lower_middle = array[x + 1:, y].tolist()
    lower_right = array[x + 1: x + 1 + min(column_max_index - x, row_max_index - y),
                    y + 1: y + 1 + min(column_max_index - x, row_max_index - y)].diagonal().tolist()

    return [upper_left, upper_middle, upper_right, middle_left, middle_right, lower_left, lower_middle, lower_right]


def first_visible_seat(array_elements):
    if len(array_elements):
        for i in array_elements:
            if i is not None:
                return i
    return 0


def make_rounds(array: np.array, max_seats_occcupied: int, adjacent: bool = True):
    changed = True
    while changed:
        new_array = change_seats(array, max_seats_occcupied, adjacent)
        changed = not np.array_equal(array, new_array)
        array = new_array.copy()
    return np.count_nonzero(array)


if __name__ == '__main__':
    input = get_input('input/day11.txt')
    occupied_seats = make_rounds(array=input, max_seats_occcupied=3, adjacent=True)
    print(f'Occupied seats after rounds: {occupied_seats}')
    occupied_visible_seats = make_rounds(array=input, max_seats_occcupied=4, adjacent=False)
    print(f'Occupied visible seats: {occupied_visible_seats}')

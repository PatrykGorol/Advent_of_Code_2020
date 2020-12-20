from re import compile
from typing import List


def get_input(path: str):
    input = []
    with open(path, "r") as f:
        for line in f.readlines():
            input.append(line.strip())
    return input


def get_parameters(line: str, regex: str) -> dict:
    pattern = compile(regex)
    parameters = pattern.fullmatch(line)
    return {'start': int(parameters.group(1)),
            'stop': int(parameters.group(2)),
            'letter': parameters.group(3),
            'password': parameters.group(4)}


def validate_password(start: int, stop: int, letter: str, password: str) -> bool:
    pattern = compile(f'[{letter}]')
    occurences = len(pattern.findall(password))
    return start <= occurences <= stop


def validate_password_with_positions(start: int, stop: int, letter: str, password: str) -> bool:
    position_1 = start
    position_2 = stop
    return sum([1 if position < len(password) and password[position] == letter else 0 for position in
                (position_1 - 1, position_2 - 1)]) == 1


def count_valid_passwords(input: List[str], regex: str, func) -> int:
    counter = 0
    for line in input:
        parameters = get_parameters(line, regex)
        counter += int(func(**parameters))
    return counter


if __name__ == '__main__':
    path = 'input/day2.txt'
    input = get_input(path)
    regex = '([0-9]+)\-([0-9]+) ([a-z]+): ([a-z]+)'
    counter = count_valid_passwords(input, regex, validate_password)
    print(f'Liczba poprawnych haseł (liczba wystąpień): {counter}')
    counter_with_positions = count_valid_passwords(input, regex, validate_password_with_positions)
    print(f'Liczba poprawnych haseł (pozycje): {counter_with_positions}')

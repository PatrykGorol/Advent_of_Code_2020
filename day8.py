import copy
import re
from typing import List, Dict, Union, Tuple, Optional


def get_input(path: str) -> List[Dict[str, Union[str, int, bool]]]:
    pattern = re.compile('([a-z]+) ([+-][0-9]+)')
    input = []
    with open(path, "r") as f:
        for line in f.readlines():
            params = pattern.fullmatch(line.strip())
            input.append({'action': params.group(1), 'value': int(params.group(2)), 'visited': False})
    return input


def loop_sequence(input: List[Dict[str, Union[str, int, bool]]]) -> Tuple[int, int]:
    accumulator = 0
    index = 0
    while index < len(input) and not input[index]['visited']:
        input[index]['visited'] = True
        accumulator, index = execute_instruction(accumulator, index, input[index]['action'], input[index]['value'])
    return accumulator, index


def execute_instruction(accumulator: int, index: int, action: str, value: int) -> Tuple[int, int]:
    if action == 'acc':
        accumulator += value
        index += 1
    elif action == 'jmp':
        index += value
    else:
        index += 1
    return accumulator, index


def repair_loop(input: List[Dict[str, Union[str, int, bool]]]) -> Optional[int]:
    input_length = len(input)
    new_input = copy.deepcopy(input)
    for i in range(input_length):
        if new_input[i]['action'] == 'nop':
            new_input[i]['action'] = 'jmp'
        elif new_input[i]['action'] == 'jmp':
            new_input[i]['action'] = 'nop'
        else:
            continue
        accumulator, index = loop_sequence(new_input)
        if index == input_length:
            return accumulator
        new_input = copy.deepcopy(input)
    return None


def clear_visits(input: List[Dict[str, Union[str, int, bool]]]) -> None:
    for i in input:
        if i['visited']:
            i['visited'] = False
    return None


if __name__ == '__main__':
    input = get_input('input/day8.txt')
    accumulator, index = loop_sequence(input)
    print(f'Value of accumulator in broken loop: {accumulator}')

    clear_visits(input)
    accumulator_from_repaired_loop = repair_loop(input)
    print(f'Value of accumulator in repaired loop: {accumulator_from_repaired_loop}')

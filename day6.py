from typing import List


def get_input(path: str):
    with open(path, "r") as f:
        input = f.read().split('\n\n')
    input = [line.strip().split('\n') for line in input]
    return input


def count_answers_for_group(group: List[str], intersection: bool):
    if intersection:
        return len(set.intersection(*[set(i) for i in group]))
    return len(set(''.join(group)))


def sum_answers_in_all_groups(input: List[List[str]], intersection: bool = False):
    return sum((count_answers_for_group(group, intersection) for group in input))


if __name__ == '__main__':
    input = get_input('input/day6.txt')
    all_answers = sum_answers_in_all_groups(input)
    print(f'Sum of answers in all groups: {all_answers}')
    all_answers_intersection = sum_answers_in_all_groups(input, intersection=True)
    print(f'Sum of answers in all groups with intersection: {all_answers_intersection}')

import re
from typing import List, Dict, Union, Optional

from day2 import get_input


def extract_data_from_input(input: List[str]):
    main_pattern = re.compile('([a-z]+ [a-z]+) bags contain (.+)')
    minor_pattern = re.compile('([0-9]+) ([a-z]+ [a-z]+) bags?[.,] ?')
    rules = []
    for line in input:
        main_bag, inside_bags = main_pattern.fullmatch(line).groups()
        if inside_bags != 'no other bags.':
            inside_bags = {bag: int(q) for (q, bag) in minor_pattern.findall(inside_bags)}
            value = None
        else:
            inside_bags = {}
            value = 0
        rules.append({'main_bag': main_bag, 'inside_bags': inside_bags, 'value': value})
    return rules


def count_bags_containing(bag_color: str, rules: List[Dict[str, Union[str, Dict[str, str], Optional[int]]]]):
    colors = [bag_color, ]
    while len(colors):
        new_colors = []
        for rule in rules:
            if rule['value'] is None:
                for color in colors:
                    if color in rule['inside_bags'].keys():
                        rule['value'] = 1
                        new_colors.append(rule['main_bag'])
                        break
        colors = list(set(new_colors))
    return sum((rule['value'] for rule in rules if rule['value'] is not None))


def count_bags_inside(bag_color: str, rules: List[Dict[str, Union[str, Dict[str, str], Optional[int]]]]):
    for rule in rules:
        if rule['main_bag'] == bag_color:
            if len(rule['inside_bags']) == 0:
                return 0
            return sum((rule['inside_bags'][bag] + rule['inside_bags'][bag] * count_bags_inside(bag, rules) for bag in
                        rule['inside_bags'].keys()))


if __name__ == '__main__':
    input = get_input('input/day7.txt')
    rules = extract_data_from_input(input)
    counter_for_containing_bags = count_bags_containing('shiny gold', rules)
    print(f'Bags containing: {counter_for_containing_bags}')
    counter_for_inside_bags = count_bags_inside('shiny gold', rules)
    print(f'Bags inside: {counter_for_inside_bags}')

from typing import List, Dict, Tuple
from re import compile

fields = {'byr': compile('19[2-9][0-9]|200[0-2]'),
          'iyr': compile('201[0-9]|2020'),
          'eyr': compile('202[0-9]|2030'),
          'hgt': compile('1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in'),
          'hcl': compile('#[0-9a-f]{6}'),
          'ecl': compile('amb|blu|brn|gry|grn|hzl|oth'),
          'pid': compile('[0-9]{9}'),
          'cid': 0}


def get_input(path: str):
    with open(path, "r") as f:
        input = f.read().split('\n\n')
    input = [line.strip().replace('\n', ' ') for line in input]
    return input


def convert_input_to_dict(input: List[str]):
    input_dict = []
    pattern = compile('([a-z]+):([^ ]+)')
    for i in input:
        input_dict.append({key: value for (key, value) in pattern.findall(i)})
    return input_dict


def count_valid_passports(input_dict: List[Dict[str, str]], check_patterns: bool = False):
    required_fields = tuple(field for field in fields.keys() if fields[field] != 0)
    counter = 0
    for passport in input_dict:
        counter += validate_passport(passport, required_fields, check_patterns)
    return counter


def validate_passport(passport: Dict[str, str], required_fields: Tuple[str], check_patterns: bool):
    if all(field in passport.keys() for field in required_fields):
        if not check_patterns:
            return True
        for f in required_fields:
            if fields[f].fullmatch(passport[f]) is None:
                return False
        return True
    return False


if __name__ == '__main__':
    input = get_input('input/day4.txt')
    input_dict = convert_input_to_dict(input)
    counter = count_valid_passports(input_dict)
    print(f'Liczba prawidłowych paszportów: {counter}')
    counter_with_patterns = count_valid_passports(input_dict, check_patterns=True)
    print(f'Liczba prawidłowych paszportów (uwzględniając dodatkowe warunki: {counter_with_patterns}')

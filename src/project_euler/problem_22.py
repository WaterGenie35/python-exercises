import os
from typing import List


def solution():
    """
    Solution to Project Euler problem 22
    https://projecteuler.net/problem=22

    Find the sum of name scores in the given file.
    For an element in a list of string, its name score is the product of:
      - its order in the list when sorted alphabetically
      - the sum of the value of each characters in the name
        (with a, b, ..., z having values 1, 2, ..., 26 respectively)
    """
    print(sum_of_name_scores(parse_names("problem_22_names.txt")))


def test_solution():
    assert sum_of_name_scores(parse_names("problem_22_names.txt")) == 871_198_282


def parse_names(filename: str) -> List[str]:
    names = []
    current_dir = os.path.dirname(__file__)
    filepath = os.path.join(current_dir, filename)
    with open(filepath) as file:
        for line in file:
            names.extend([name.strip("\"").lower() for name in line.split(",")])
    return names


def sum_of_name_scores(names: List[str]) -> int:
    sorted_names = sorted(names)
    score_sum = 0
    for i, name in enumerate(sorted_names):
        score_sum += (i + 1) * name_value(name)
    return score_sum


def name_value(name: str) -> int:
    return sum([ord(char.lower()) - 96 for char in name])

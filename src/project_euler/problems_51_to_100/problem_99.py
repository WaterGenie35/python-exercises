import os
from typing import List, Tuple


def solution():
    """
    Solution to Project Euler problem 99
    https://projecteuler.net/problem=99
    """
    print(largest_line(parse_base_exponent_pairs("problem_99_base_exp.txt")))


def test_solution():
    assert largest_line(parse_base_exponent_pairs("problem_99_base_exp.txt")) == 709


def parse_base_exponent_pairs(filename: str) -> List[Tuple[int, int]]:
    pairs = []
    current_dir = os.path.dirname(__file__)
    filepath = os.path.join(current_dir, filename)
    with open(filepath) as file:
        for line in file:
            base_str, exponent_str = line.strip().split(",")
            pairs.append((int(base_str), int(exponent_str)))
    return pairs


def largest_line(pairs: Tuple[int, int]) -> int:
    if len(pairs) == 0:
        return 0

    line = 1
    base_of_largest = pairs[0][0]
    exponent_of_largest = pairs[0][1]
    for i, pair in enumerate(pairs[1:]):
        base_of_new = pair[0]
        exponent_of_new = pair[1]
        if base_of_new ** (exponent_of_new / exponent_of_largest) > base_of_largest:
            base_of_largest = base_of_new
            exponent_of_largest = exponent_of_new
            line = i + 2

    return line

import os
from collections.abc import Iterable
from typing import List


def solution():
    """
    Solution to Project Euler problem 42
    https://projecteuler.net/problem=42

    Find the number of triangle words in the given file.
    A word is triangle if when converting each letter to a number corresponding
    to its alphabetical position (a -> 1, b -> 2, ..., z -> 26), the sum is a
    triangle number.
    THe nth triangle number is given by n(n+1)/2.
    """
    print(num_triangle_words(parse_words("problem_42_words.txt")))


def test_solution():
    assert num_triangle_words(parse_words("problem_42_words.txt")) == 162


def parse_words(filename: str) -> List[str]:
    words = []
    current_dir = os.path.dirname(__file__)
    filepath = os.path.join(current_dir, filename)
    with open(filepath) as file:
        for line in file:
            words.extend(word.strip("\"").lower() for word in line.split(","))
    return words


def num_triangle_words(words: List[str]) -> int:
    num_words = 0
    triangulars = set()
    triangular_generator = generate_triangular_numbers()
    largest_triangular = 0
    for word in words:
        value = word_value(word)
        while largest_triangular < value:
            triangular_number = next(triangular_generator)
            triangulars.add(triangular_number)
            largest_triangular = triangular_number
        if value in triangulars:
            num_words += 1
    return num_words


def word_value(word: str) -> int:
    return sum(ord(char) - 96 for char in word)


def generate_triangular_numbers() -> Iterable[int]:
    triangular_number = 0
    head = 0
    while True:
        head += 1
        triangular_number += head
        yield triangular_number

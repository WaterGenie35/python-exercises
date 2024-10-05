from math import factorial
from typing import List


def solution():
    """
    Solution to Project Euler problem 24
    https://projecteuler.net/problem=24

    Find the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
    6, 7, 8, and 9.
    Permutations are in lexicographic order if they are listed numerically or
    alphabetically.
    """
    print(nth_lexicographic_permutation(1_000_000, [str(i) for i in range(0, 10)]))


def test_solution():
    assert nth_lexicographic_permutation(17, ["0", "1", "2", "3"]) == "2301"
    assert nth_lexicographic_permutation(1_000_000, [str(i) for i in range(0, 10)]) == "2783915460"


def nth_lexicographic_permutation(n: str, elements: List[str]) -> str:
    num_elements = len(elements)
    num_perms = factorial(num_elements)
    remaining_elements = sorted(elements)
    section_divider = num_perms
    section_index = n - 1
    perm = []
    for i in range(1, num_elements):
        section_divider //= num_elements - i + 1
        digit_index = section_index // section_divider
        section_index %= section_divider
        perm.append(remaining_elements[digit_index])
        remaining_elements = remaining_elements[:digit_index] + remaining_elements[digit_index + 1 :]
    perm.append(remaining_elements[0])
    return "".join(perm)

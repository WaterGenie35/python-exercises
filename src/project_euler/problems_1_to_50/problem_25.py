from math import log10

from utils.math import num_of_digits


def solution():
    """
    Solution to Project Euler problem 25
    https://projecteuler.net/problem=25

    Find the index of the first Fibonacci number with 1_000 digits.
    Start the Fibonacci sequence with 1 and 1.
    """
    print(index_of_first_fibonacci_with_num_digits_gte(1_000))


def test_solution():
    assert index_of_first_fibonacci_with_num_digits_gte(3) == 12
    assert index_of_first_fibonacci_with_num_digits_gte(1_000) == 4_782


def index_of_first_fibonacci_with_num_digits_gte(min_digits: int) -> int:
    if min_digits == 1:
        return 1
    prev = 1
    head = 1
    index = 2
    while num_of_digits(head) < min_digits:
        tmp = head
        head = head + prev
        prev = tmp
        index += 1
    return index

from utils.math import sum_of_digits


def solution():
    """
    Solution to Project Euler problem 16
    https://projecteuler.net/problem=16

    Find the sum of the digits of 2^1_000.
    """
    print(sum_of_digits(2**1_000))


def test_solution():
    assert sum_of_digits(2**1_000) == 1_366

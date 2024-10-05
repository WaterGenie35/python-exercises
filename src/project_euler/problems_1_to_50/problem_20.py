from math import factorial

from utils.math import sum_of_digits


def solution():
    """
    Solution to Project Euler problem 20
    https://projecteuler.net/problem=20

    Find the sum of digits of 100!.
    """
    print(sum_of_digits(factorial(100)))


def test_solution():
    assert sum_of_digits(factorial(10)) == 27
    assert sum_of_digits(factorial(100)) == 648

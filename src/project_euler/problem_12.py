from utils.math import num_factors


def solution():
    """
    Solution to Project Euler problem 12
    https://projecteuler.net/problem=12

    Find the first triangle number to have greater than 500 divisors.
    """
    print(first_triangle_number_with_num_factors_gt(500))


def test_solution():
    assert first_triangle_number_with_num_factors_gt(5) == 28
    # TODO: still need to optimize this (test ~0.75s)
    assert first_triangle_number_with_num_factors_gt(500) == 76_576_500


def first_triangle_number_with_num_factors_gt(num_divisors: int) -> int:
    triangle_number = 0
    head = 1
    while True:
        triangle_number += head
        if num_factors(triangle_number) > num_divisors:
            return triangle_number
        head += 1

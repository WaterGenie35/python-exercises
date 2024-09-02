from utils.math import divisors_of


def solution():
    """
    Solution to Project Euler problem 12
    https://projecteuler.net/problem=12

    Find the first triangle number to have greater than 500 divisors.
    """
    print(first_triangle_number_with_num_divisors_gt(500))


def test_solution():
    assert first_triangle_number_with_num_divisors_gt(5) == 28
    # assert first_triangle_number_with_num_divisors_gt(500) == 76_576_500


def first_triangle_number_with_num_divisors_gt(num_divisors: int) -> int:
    triangle_number = 0
    head = 1
    while True:
        triangle_number += head
        if len(divisors_of(triangle_number)) > num_divisors:
            return triangle_number
        head += 1

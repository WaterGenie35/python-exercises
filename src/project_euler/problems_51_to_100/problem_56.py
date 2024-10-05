from utils.math import sum_of_digits


def solution():
    """
    Solution to Project Euler problem 56
    https://projecteuler.net/problem=56

    Find the maximum sum of digits of a natural number of the form a^b where
    a, b < 100.
    """
    print(max_digit_sum_of_power(base_lt=100, power_lt=100))


def test_solution():
    assert max_digit_sum_of_power(base_lt=100, power_lt=100) == 972


def max_digit_sum_of_power(base_lt: int, power_lt: int) -> int:
    max_digit_sum = 0
    for a in range(1, base_lt):
        for b in range(1, power_lt):
            digit_sum = sum_of_digits(a**b)
            max_digit_sum = max(max_digit_sum, digit_sum)
    return max_digit_sum

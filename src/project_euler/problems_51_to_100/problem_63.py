import math


def solution():
    """
    Solution to Project Euler problem 63
    https://projecteuler.net/problem=63
    """
    print(num_of_n_digit_nth_power())


def test_solution():
    assert num_of_n_digit_nth_power() == 49


def num_of_n_digit_nth_power() -> int:
    count = 0
    n = 1
    while True:
        start = math.ceil(10 ** ((n - 1) / n))
        end = min(9, math.floor(((10**n) - 1) ** (1 / n)))
        if start >= 10:
            break
        nums = end - start + 1
        if nums <= 0:
            break
        count += nums
        n += 1
    return count

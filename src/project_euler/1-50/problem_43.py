from utils.math import generate_pandigitals, num_of_digits


def solution():
    """
    Solution to Project Euler problem 43
    https://projecteuler.net/problem=43

    Find the sum of all 0-9 pandigital numbers such that
      d2d3d4 is divisible by 2
      d3d4d5 is divisible by 3
      d4d5d6 is divisible by 5
      d5d6d7 is divisible by 7
      d6d7d8 is divisible by 11
      d7d8d9 is divisible by 13
      d8d9d10 is divisible by 17
    where di is the ith digit.
    """
    print(sum_of_divisible_pandigitals())


# TODO: optimize
# def test_solution():
#     assert sum_of_divisible_pandigitals() == 16_695_334_890


def sum_of_divisible_pandigitals() -> int:
    sum_nums = 0
    for pandigital in generate_pandigitals(start=0, end=9):
        if is_divisible(pandigital):
            sum_nums += pandigital
    return sum_nums


def is_divisible(n: int) -> bool:
    # minor speed-up
    if (n % 1000) % 17 != 0:
        return False
    divisors = [2, 3, 5, 7, 11, 13]  # , 17]
    digits = [int(char) for char in str(n)]
    for i, divisor in enumerate(divisors):
        sub_num = (100 * digits[i + 1]) + (10 * digits[i + 2]) + digits[i + 3]
        if sub_num % divisor != 0:
            return False
    return True

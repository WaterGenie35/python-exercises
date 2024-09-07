from typing import List

from utils.math import factors_of


def solution():
    """
    Solution to Project Euler problem 23
    https://projecteuler.net/problem=23

    Find the sum of all positive integers that cannot be written as the sum of
    two abundant numbers.
    A number n is abundant if the sum of its proper divisors is greater than n.
    Note that all integers greater than 20_161 can be written as the sum of two
    abundant numbers.
    """
    print(sum_of_non_sum_of_two_abundants())


def test_solution():
    assert sum_of_non_sum_of_two_abundants() == 4_179_871


def sum_of_non_sum_of_two_abundants():
    non_sum_of_two_abundants = [True] * (20_161 + 1)
    abundant_numbers = abundant_numbers_lte(20_161)
    for i, abundant_1 in enumerate(abundant_numbers):
        for j in range(i, len(abundant_numbers)):
            abundant_2 = abundant_numbers[j]
            sum_of_abundants = abundant_1 + abundant_2
            if sum_of_abundants > 20_161:
                break
            non_sum_of_two_abundants[sum_of_abundants] = False
    return sum(i for i in range(1, 20_161 + 1) if non_sum_of_two_abundants[i])


def abundant_numbers_lte(n: int) -> List[int]:
    abundant_numbers = []
    head = 12  # smallest abundant number
    while head <= n:
        if is_abundant(head):
            abundant_numbers.append(head)
        head += 1
    return abundant_numbers


def is_abundant(n: int) -> bool:
    proper_factors = factors_of(n)[:-1]
    return sum(proper_factors) > n

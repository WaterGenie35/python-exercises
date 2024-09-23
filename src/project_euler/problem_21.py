from utils.math import is_amicable


def solution():
    """
    Solution to Project Euler problem 21
    https://projecteuler.net/problem=21

    Find the sum of all amicable numbers less than 10_000.
    Let d(n) be the sum of proper factors of n.
    A positive integer n is an amicable number if there exists a positive
    integer m (it's amicable pair) != n such that d(n) = m and d(m) = n.
    """
    print(sum_of_amicable_numbers_lt(10_000))


def test_solution():
    assert sum_of_amicable_numbers_lt(10_000) == 31_626


def sum_of_amicable_numbers_lt(max_num: int) -> int:
    # Note the pair does not necessarily have to be less than max_num.
    sum_of_amicable = 0
    for head in range(1, max_num):
        if is_amicable(head):
            sum_of_amicable += head
    return sum_of_amicable

from utils.math import primes_lte


def solution():
    """
    Solution to Project Euler problem 10
    https://projecteuler.net/problem=10

    Find the sum of primes below 2_000_000.
    Start the prime number with 2.
    """
    print(sum_of_primes_lt(2_000_000))


def test_solution():
    assert sum_of_primes_lt(10) == 17
    assert sum_of_primes_lt(2_000_000) == 142_913_828_922


def sum_of_primes_lt(max_num: int) -> int:
    return sum(primes_lte(max_num - 1))

from utils.math import generate_pandigitals, is_pandigital, is_prime, primes_lte


def solution():
    """
    Solution to Project Euler problem 41
    https://projecteuler.net/problem=41

    Find the largest n-digit pandigital prime.
    n-digit number is pandigital if it contains all digits 1 to n exactly once.
    """
    print(largest_pandigital_prime())


def test_solution():
    assert largest_pandigital_prime() == 7_652_413


def largest_pandigital_prime():
    for num_digits in range(9, 0, -1):
        for pandigital in generate_pandigitals(start=1, end=num_digits, reversed=True):
            if is_prime(pandigital):
                return pandigital
    return None

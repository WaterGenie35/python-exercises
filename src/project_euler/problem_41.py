from utils.math import is_pandigital, primes_lte


def solution():
    """
    Solution to Project Euler problem 41
    https://projecteuler.net/problem=41

    Find the largest n-digit pandigital prime.
    n-digit number is pandigital if it contains all digits 1 to n exactly once.
    """
    print(largest_pandigital_prime())


# def test_solution():
#     assert largest_pandigital_prime() == 7_652_413


# TODO: generate from digits instead of going through primes
def largest_pandigital_prime():
    primes = primes_lte(987_654_321)
    for prime in reversed(primes):
        if is_pandigital(prime, up_to_num_digits_of_n=True):
            return prime
    return None

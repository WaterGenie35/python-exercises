from utils.math import num_of_digits, primes_lte


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
        if is_pandigital(prime):
            return prime
    return None


def is_pandigital(n: int) -> bool:
    num_digits = num_of_digits(n)
    remaining = n
    digits = set()
    while remaining > 0:
        digit = remaining % 10
        if digit > num_digits or digit == 0 or digit in digits:
            return False
        digits.add(digit)
        remaining //= 10
    return True

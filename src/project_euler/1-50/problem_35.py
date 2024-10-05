from utils.math import num_of_digits, primes_lte
from utils.search import binary_search


def solution():
    """
    Solution to Project Euler problem 35
    https://projecteuler.net/problem=35

    Find the number of circular primes below 1_000_000.
    A number is a circular prime if all rotations of the digits are prime.
    """
    print(num_circular_primes_lt(1_000_000))


def test_solution():
    assert num_circular_primes_lt(100) == 13
    assert num_circular_primes_lt(1_000_000) == 55


def num_circular_primes_lt(upper_bound: int) -> int:
    # Note number < upper_bound may have a rotation >= upper_bound
    digits = num_of_digits(upper_bound - 1)
    primes = primes_lte(10**digits - 1)

    num_circular = 0
    for prime in primes:
        prime_str = str(prime)
        is_circular = True
        for head in range(1, len(prime_str)):
            rotated = int(prime_str[head:] + prime_str[:head])
            if binary_search(primes, rotated) is None:
                is_circular = False
                break
        if is_circular:
            num_circular += 1
    return num_circular

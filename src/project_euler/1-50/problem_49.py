from utils.math import is_permutation, primes_lte
from utils.search import binary_search


def solution():
    """
    Solution to Project Euler problem 49
    https://projecteuler.net/problem=49

    Find the 12-digit number formed by concatenating the 3 terms in the
    arithmetic sequence of 4-digit numbers in which all the terms are prime,
    each number is a permutation of the other, and it's not the 1_487, 4_817,
    and 8_147 sequence.
    """
    print(concatenated_4_digit_prime_and_permuted_arithmetic_sequence())


def test_solution():
    assert concatenated_4_digit_prime_and_permuted_arithmetic_sequence() == 2969_6299_9629


def concatenated_4_digit_prime_and_permuted_arithmetic_sequence() -> int:
    primes = primes_lte(9_999)
    start = binary_search(primes, 1_487) + 1
    for i in range(start, len(primes) - 2):
        p1 = primes[i]
        for j in range(i + 1, len(primes) - 1):
            p2 = primes[j]
            if not is_permutation(p1, p2):
                continue

            d = p2 - p1
            p3 = p2 + d
            if p3 in primes and is_permutation(p2, p3):
                return (p1 * 10**8) + (p2 * 10**4) + p3

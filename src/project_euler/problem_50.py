from utils.math import primes_lte
from utils.search import binary_search


def solution():
    """
    Solution to Project Euler problem 50
    https://projecteuler.net/problem=50

    Find a prime below 1_000_000 that can be written as the sum of the most
    number of consecutive primes.
    """
    print(consecutive_prime_sum_lt(1_000_000))


def test_solution():
    assert consecutive_prime_sum_lt(100) == 41
    assert consecutive_prime_sum_lt(1_000) == 953
    assert consecutive_prime_sum_lt(1_000_000) == 997_651


def consecutive_prime_sum_lt(upper_bound: int) -> int:
    primes = primes_lte(upper_bound - 1)
    num_terms = len(primes) - 1
    base_sum = sum(primes)
    while num_terms > 1:
        head = 0
        tail = num_terms - 1
        base_sum -= primes[num_terms]
        moving_sum = base_sum
        for i in range(len(primes) - num_terms + 1):
            if i > 0:
                moving_sum -= primes[head + i - 1]
                moving_sum += primes[tail + i]
            if moving_sum > primes[-1]:
                break
            if binary_search(primes[tail + i :], moving_sum) is not None:
                return moving_sum
        head += 1
        num_terms -= 1

    return None

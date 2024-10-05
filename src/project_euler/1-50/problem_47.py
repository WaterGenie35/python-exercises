from utils.math import generate_primes


def solution():
    """
    Solution to Project Euler problem 47
    https://projecteuler.net/problem=47

    Find the first number of the first 4 consecutive integers to have 4
    distinct prime factors each.
    """
    print(first_of_first_n_consecutive_int_with_k_distinct_prime_factors(n=4, k=4))


def test_solution():
    assert first_of_first_n_consecutive_int_with_k_distinct_prime_factors(n=2, k=2) == 14
    assert first_of_first_n_consecutive_int_with_k_distinct_prime_factors(n=3, k=3) == 644
    # TODO: optimize?
    # assert first_of_first_n_consecutive_int_with_k_distinct_prime_factors(n=4, k=4) == 134_043


def first_of_first_n_consecutive_int_with_k_distinct_prime_factors(n: int, k: int) -> int:
    primes = []
    last_prime = None
    prime_generator = generate_primes()

    head = 2
    consecutive_nums = 0
    while consecutive_nums < n:
        # Append to list of primes as necessary
        while len(primes) == 0 or last_prime < head:
            last_prime = next(prime_generator)
            primes.append(last_prime)

        remaining = head
        distinct_prime_factors = 0
        for prime in primes:
            if remaining % prime != 0:
                continue
            distinct_prime_factors += 1
            if distinct_prime_factors > k:
                break
            while remaining % prime == 0:
                remaining //= prime

        if distinct_prime_factors != k:
            consecutive_nums = 0
        else:
            consecutive_nums += 1

        head += 1

    first_of_n_consecutive = head - n
    return first_of_n_consecutive

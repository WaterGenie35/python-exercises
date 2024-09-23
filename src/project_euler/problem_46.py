from utils.math import generate_primes
from utils.search import binary_search


def solution():
    """
    Solution to Project Euler problem 46
    https://projecteuler.net/problem=46

    Find the smallest odd composite number that cannot be written as the sum of
    a prime and twice a square.
    """
    print(smallest_odd_composite_non_sum_of_prime_and_twice_square())


def test_solution():
    assert smallest_odd_composite_non_sum_of_prime_and_twice_square() == 5_777


def smallest_odd_composite_non_sum_of_prime_and_twice_square() -> int:
    primes = []
    last_prime = None
    prime_generator = generate_primes()

    twice_squares = [2]
    last_num_for_twice_square = 1

    odd_composite = 3

    found = False
    while not found:
        # Append to lists of primes and twice squares as necessary
        while len(primes) == 0 or last_prime < odd_composite:
            last_prime = next(prime_generator)
            primes.append(last_prime)
        if last_prime == odd_composite:
            odd_composite += 2
            continue

        while 2 * (last_num_for_twice_square**2) < odd_composite:
            last_num_for_twice_square += 1
            twice_squares.append(2 * (last_num_for_twice_square**2))

        non_sum = True
        for prime in primes:
            complement = odd_composite - prime
            matching_index_of_twice_square = binary_search(twice_squares, complement)
            if matching_index_of_twice_square is not None:
                non_sum = False
                break

        if non_sum:
            found = True
            break

        odd_composite += 2

    return odd_composite

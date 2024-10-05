from collections.abc import Iterator

from utils.math import generate_primes, num_of_digits
from utils.search import binary_search


def solution():
    """
    Solution to Project Euler problem 51
    https://projecteuler.net/problem=51
    """
    print(prime_digit_replacements(num_primes=8))


# TODO: optimize
# def test_solution():
#     assert prime_digit_replacements(num_primes=7) == 56_003
#     assert prime_digit_replacements(num_primes=8) == 121_313


def prime_digit_replacements(num_primes: int) -> int:
    head = 11
    head_index = 4
    head_prime = None
    prime_generator = generate_primes()
    primes = []
    found = False
    while not found:
        # Generate primes to current number of digits as we go along
        num_digits = num_of_digits(head)
        current_magnitude = 10**num_digits
        while len(primes) == 0 or primes[-1] < current_magnitude:
            primes.append(next(prime_generator))

        for binary_perm in generate_digit_replacements(num_digits):
            start = 0 if binary_perm[0] == "0" else 1
            primes_count = 0
            head_prime = None
            for n in range(start, 10):
                replaced = list(str(head))
                for i, replace in enumerate(binary_perm):
                    if replace == "1":
                        replaced[i] = str(n)
                replaced = int("".join(replaced))
                if binary_search(primes, replaced) is not None:
                    primes_count += 1
                    if head_prime is None:
                        head_prime = replaced
            if primes_count == num_primes:
                found = True
                break

        head_index += 1
        head = primes[head_index]

    return head_prime


def generate_digit_replacements(num_digits: int) -> Iterator[str]:
    for perm in range(1, (2**num_digits) - 1):
        yield format(perm, f'0{num_digits}b')

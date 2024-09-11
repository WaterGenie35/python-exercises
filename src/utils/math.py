from collections.abc import Iterator
from math import log10
from typing import List

from utils.prime_table import PRIMES


def is_prime(n: int) -> bool:
    # All primes > 3 can be written as 6k+-1 for some positive k
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n < 9:
        return True

    factor = 5
    while factor**2 <= n:
        if n % factor == 0 or n % (factor + 2) == 0:
            return False
        factor += 6
    return True


def nth_prime(n: int) -> int:
    if n == 1:
        return 2
    i = 2
    head = 3
    while i < n:
        head += 2
        if is_prime(head):
            i += 1
    return head


def generate_primes() -> Iterator[int]:
    yield 2
    yield 3
    head = 5
    while True:
        if is_prime(head):
            yield head
        if is_prime(head + 2):
            yield head + 2
        head += 6


def primes_lte(n: int) -> List[int]:
    # Sieve of Eratosthenes
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    # With improvements:
    #  - Starting from p**2
    #  - Ending when p**2 > n
    #  - Going by odd p
    # If we still need to optimize further, see "wheel factorization"
    # or Euler's sieve.
    num_odds = (n // 2) - ((n + 1) % 2)
    primes_sieve = [True] * num_odds

    odd = 3
    while odd**2 <= n:
        odd_index = (odd // 2) - 1
        if primes_sieve[odd_index]:
            head = odd**2
            while head <= n:
                if head % 2 == 1:
                    head_index = (head // 2) - 1
                    primes_sieve[head_index] = False
                head += odd
        odd += 2

    primes = []
    if n >= 2:
        primes.append(2)
    primes.extend([(2 * i) + 3 for i, prime_index in enumerate(primes_sieve) if prime_index])
    return primes


def factors_of(n: int) -> List[int]:
    divisors = []
    pairs = []
    head = 1
    while head**2 <= n:
        if n % head == 0:
            divisors.append(head)
            factor_pair = n // head
            if head != factor_pair:
                pairs.append(factor_pair)
        head += 1
    divisors.extend(reversed(pairs))
    return divisors


def num_factors(n: int) -> int:
    # See https://en.wikipedia.org/wiki/Divisor_function
    if n in PRIMES or is_prime(n):
        return 2

    num = 1
    # Use pre-computed table of primes as long as n is sufficiently small
    primes = PRIMES if n <= PRIMES[-1] ** 2 else primes_lte(n)
    remaining = n
    for prime in primes:
        exponent = 0
        while remaining % prime == 0:
            exponent += 1
            remaining //= prime
        num *= exponent + 1
        if prime**2 > n:
            break
    return num


def greatest_common_factor(a: int, b: int) -> int:
    if a == 0 and b == 0:
        return 0
    if a == 0 or b == 0:
        return max(abs(a), abs(b))

    head = min(a, b)
    remainder = max(a, b) % head
    while remainder > 0:
        tmp = max(head, remainder)
        head = min(head, remainder)
        remainder = tmp % head
    return head


def is_amicable(n: int) -> int:
    if n == 1:
        return False
    proper_factors = factors_of(n)[:-1]

    pair = sum(proper_factors)
    if pair == 1 or n == pair:
        return False
    pair_proper_factors = factors_of(pair)[:-1]
    return n == sum(pair_proper_factors)


def choose(n: int, k: int) -> int:
    product = 1
    bound = min(k, n - k) + 1
    for i in range(1, bound):
        product *= (n + 1.0 - i) / i
    return round(product)


def num_of_digits(n: int) -> int:
    if n == 0:
        return 1
    return 1 + int(log10(abs(n)))


def sum_of_digits(n: int) -> int:
    s = 0
    remaining = n
    while remaining > 0:
        s += remaining % 10
        remaining //= 10
    return s

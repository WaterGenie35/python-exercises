from typing import List


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


# TODO: optimize? see problem 12
def divisors_of(n: int) -> List[int]:
    divisors = []
    pairs = []
    head = 1
    while head**2 <= n:
        if n % head == 0:
            divisors.append(head)
            factor_pair = n / head
            if head != factor_pair:
                pairs.append(factor_pair)
        head += 1
    divisors.extend(reversed(pairs))
    return divisors


def choose(n: int, k: int) -> int:
    product = 1
    bound = min(k, n - k) + 1
    for i in range(1, bound):
        product *= (n + 1.0 - i) / i
    return round(product)

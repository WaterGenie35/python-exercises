from utils.math import is_prime


def solution():
    """
    Solution to Project Euler problem 3
    https://projecteuler.net/problem=3

    Find the largest prime factor of 600_851_475_143.
    """
    print(largest_prime_factor_of(600_851_475_143))


def test_solution():
    assert largest_prime_factor_of(13_195) == 29
    assert largest_prime_factor_of(600_851_475_143) == 6_857


def largest_prime_factor_of(n: int) -> int:
    largest_prime_factor = None
    head = 2
    if n % head == 0:
        largest_prime_factor = head
    head += 1

    while head**2 <= n:
        is_factor = n % head == 0
        if is_factor and is_prime(head):
            largest_prime_factor = head

        # Since we start from smallest head, the first prime factor pair found
        # will be the largest
        factor_pair = n / head
        if is_factor and is_prime(factor_pair):
            return factor_pair

        head += 2

    return largest_prime_factor

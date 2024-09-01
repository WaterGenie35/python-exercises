from utils.math import is_prime


def solution():
    """
    Solution to Project Euler problem 10
    https://projecteuler.net/problem=10

    Find the sum of primes below 2_000_000.
    Start the prime number with 2.
    """
    print(sum_of_primes_lt(2_000_000))


def sum_of_primes_lt(max_num: int) -> int:
    sum_of_primes = 0
    head = 2
    while head < max_num:
        if is_prime(head):
            sum_of_primes += head
        if head == 2:
            head += 1
        else:
            head += 2
    return sum_of_primes

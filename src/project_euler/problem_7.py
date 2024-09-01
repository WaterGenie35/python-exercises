from utils.math import nth_prime


def solution():
    """
    Solution to Project Euler problem 7
    https://projecteuler.net/problem=7

    Find the 10_001st prime number.
    Start the prime number with 2.
    """
    print(nth_prime(10_001))

import math


def solution():
    """
    Solution to Project Euler problem 9
    https://projecteuler.net/problem=9

    Find the product of a Pythagorean triplet whose sum is 1_000.
    A Pythagorean triplet is a set of 3 natural numbers a < b < c where
    a^2 + b^2 = c^2.
    """
    print(product_of_pythagorean_with_triplet_sum(1_000))


def product_of_pythagorean_with_triplet_sum(triplet_sum: int) -> int:
    a = 1
    product = None
    while a < triplet_sum / 3:
        b = 2
        while b < math.ceil((triplet_sum - a) / 2):
            c = triplet_sum - (a + b)
            if a**2 + b**2 == c**2:
                product = a * b * c
            b += 1
        a += 1
    return product

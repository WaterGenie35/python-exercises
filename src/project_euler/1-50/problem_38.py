from utils.math import is_pandigital, num_of_digits


def solution():
    """
    Solution to Project Euler problem 38
    https://projecteuler.net/problem=38

    Find the largest 1-9 9-digit pandigital number that can be formed as a
    concatenated product of an integer with (1, 2, ..., n) where n > 1.
    """
    print(concatenated_product_pandigital())


def test_solution():
    assert concatenated_product_pandigital() == 932_718_654


def concatenated_product_pandigital() -> int:
    largest_pandigital = 0
    # For minimal n = 2, the minimal concatenation of x and 2x is 1_000_020_000
    # which contains more than 9 digits.
    for x in range(1, 10_000):
        for n in range(2, 10):
            concatenated_product = 0
            for i in range(1, n + 1):
                product = x * i
                product_digits = num_of_digits(product)
                concatenated_product *= 10**product_digits
                concatenated_product += product
            if concatenated_product > 987_654_321:
                continue
            if is_pandigital(concatenated_product):
                largest_pandigital = max(largest_pandigital, concatenated_product)
    return largest_pandigital

from utils.math import is_pandigital


def solution():
    """
    Solution to Project Euler problem 32
    https://projecteuler.net/problem=32

    Find the sum of products whose multiplicand-multiplier-product identity
    collectively use all the digits 1 to 9 exactly once.
    """
    print(sum_of_products_with_pandigital_identity())


def test_solution():
    assert sum_of_products_with_pandigital_identity() == 45_228


def sum_of_products_with_pandigital_identity() -> int:
    sum_of_products = 0
    products = set()
    # Note either term can't be more than 4 digits, e.g. minimum:
    # 13_456 * 2 = 26_912 with 10 digits total.
    max_term = 9_876
    for term_1 in range(1, max_term + 1):
        for term_2 in range(term_1 + 1, max_term + 1):
            product = term_1 * term_2
            if product > max_term:
                break
            concatenated = int("".join([str(term_1), str(term_2), str(product)]))
            if product not in products and is_pandigital(concatenated):
                products.add(product)
                sum_of_products += product
    return sum_of_products

from typing import List


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
            if product not in products and is_pandigital([term_1, term_2, product]):
                products.add(product)
                sum_of_products += product
    return sum_of_products


def is_pandigital(nums: List[int]) -> bool:
    joined_num = "".join([str(num) for num in nums])
    if len(joined_num) != 9:
        return False
    digits = {str(d): 0 for d in range(1, 10)}
    for char in joined_num:
        if char == "0" or digits[char] == 1:
            return False
        digits[char] = 1
    return True

from utils.string import is_palindrome


def solution():
    """
    Solution to Project Euler problem 4
    https://projecteuler.net/problem=4

    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    print(largest_palindrome_product_from_digits(3))


def test_solution():
    assert largest_palindrome_product_from_digits(2) == 9009
    assert largest_palindrome_product_from_digits(3) == 906609


def largest_palindrome_product_from_digits(max_digits: int) -> int:
    largest_palindrome_product = None

    largest_term = 10**max_digits - 1
    smallest_term = 10 ** (max_digits - 1)

    term_1 = largest_term
    term_2 = largest_term
    while term_1 >= smallest_term:
        while term_2 >= smallest_term:
            product = term_1 * term_2
            if is_palindrome(str(product)):
                if largest_palindrome_product is None or product > largest_palindrome_product:
                    largest_palindrome_product = product
                break
            term_2 -= 1
        term_1 -= 1
        term_2 = term_1

    return largest_palindrome_product

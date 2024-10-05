from math import isclose

from utils.math import greatest_common_factor, num_of_digits


def solution():
    """
    Solution to Project Euler problem 33
    https://projecteuler.net/problem=33

    Find the denominator of the product of all the 2-digit curious fractions
    in its lowest common terms.
    An n-digit curious fraction is a fraction less than 1 such that both the
    numerator and the denominator has n digits and there's a digit in both
    the numerator and the denominator, not zero in the 1st digit of both, in
    which the fraction is equal to a new fraction with an instance of that
    digit removed from both the numerator and the denominator.
    """
    print(denominator_of_reduced_product_of_curious_fractions_with_digit(2))


def test_solution():
    assert is_curious(49, 98)
    assert not is_curious(40, 98)
    assert not is_curious(30, 50)

    assert denominator_of_reduced_product_of_curious_fractions_with_digit(2) == 100


def denominator_of_reduced_product_of_curious_fractions_with_digit(digit: int) -> int:
    min_num = 10 ** (digit - 1)
    max_num = (10**digit) - 1
    product_numerator = 1
    product_denominator = 1
    for numerator in range(min_num, max_num):
        for denominator in range(numerator + 1, max_num + 1):
            if not is_curious(numerator, denominator):
                continue

            product_numerator *= numerator
            product_denominator *= denominator
    gcf = greatest_common_factor(product_numerator, product_denominator)
    return product_denominator // gcf


def is_curious(numerator: int, denominator: int) -> bool:
    if numerator >= denominator or num_of_digits(numerator) != num_of_digits(denominator):
        return False

    original_fraction = numerator / denominator
    numerator_digits = [d for d in str(numerator)]
    denominator_digits = [d for d in str(denominator)]
    last_digit_index = len(numerator_digits) - 1
    for i, digit_n in enumerate(numerator_digits):
        for j, digit_d in enumerate(denominator_digits):
            if digit_n != digit_d:
                continue
            if digit_n == "0" and i == last_digit_index and j == last_digit_index:
                continue

            cancelled_numerator = int("".join(numerator_digits[:i] + numerator_digits[i + 1 :]))
            cancelled_denominator = int("".join(denominator_digits[:j] + denominator_digits[j + 1 :]))
            if cancelled_numerator >= cancelled_denominator:
                continue

            cancelled_fraction = cancelled_numerator / cancelled_denominator
            if isclose(cancelled_fraction, original_fraction):
                return True

    return False

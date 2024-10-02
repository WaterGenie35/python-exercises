from utils.math import num_of_digits


def solution():
    """
    Solution to Project Euler problem 57
    https://projecteuler.net/problem=57
    """
    print(num_fractions_with_numerator_digits_gt_denominator_digits(iterations=1_000))


def test_solution():
    assert num_fractions_with_numerator_digits_gt_denominator_digits(iterations=4) == 0
    assert num_fractions_with_numerator_digits_gt_denominator_digits(iterations=8) == 1
    assert num_fractions_with_numerator_digits_gt_denominator_digits(iterations=1_000) == 153


def num_fractions_with_numerator_digits_gt_denominator_digits(iterations: int) -> int:
    # https://math.stackexchange.com/a/730378
    # For p/q, next one is (p + 2q) / (p + q)
    count = 0
    numerator = 1
    denominator = 1
    for _ in range(iterations):
        tmp = numerator
        numerator += 2 * denominator
        denominator += tmp
        if num_of_digits(numerator) > num_of_digits(denominator):
            count += 1
    return count

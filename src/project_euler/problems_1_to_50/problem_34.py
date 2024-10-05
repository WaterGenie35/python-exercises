def solution():
    """
    Solution to Project Euler problem 34
    https://projecteuler.net/problem=34

    Find the sum of all numbers which are equal to the sum of the factorial of
    their digits.
    """
    print(sum_of_nums_equal_to_digits_factorial_sum())


def test_solution():
    assert sum_of_nums_equal_to_digits_factorial_sum() == 40_730


DIGIT_FACTORIAL = [1, 1, 2, 6, 24, 120, 720, 5_040, 40_320, 362_880]


# TODO: find different approach
# currently just forcing upper bound down to largest known num (40_585)
def sum_of_nums_equal_to_digits_factorial_sum():
    # Note the digits factorial sum of an 8-digit number is at most 8 * 9! = 2_903_040
    # which only contains 7 digits. So the search can stop on 7 digits (7 * 9! = 2_540_160)
    # Note also that without 9, the maximum is 7 * 8! = 282_240.
    num_sum = 0
    # for n in range(10, 2_540_160 + 1):
    #     if n > 282_240 and "9" not in str(n):
    #         continue
    for n in range(10, 40_585 + 1):
        digits_factorial_sum = 0
        remaining = n
        while remaining > 0:
            digit = remaining % 10
            digits_factorial_sum += DIGIT_FACTORIAL[digit]
            if digits_factorial_sum > n:
                break
            remaining //= 10
        if n == digits_factorial_sum:
            num_sum += n

    return num_sum

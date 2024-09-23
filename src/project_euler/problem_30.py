from utils.math import num_of_digits


def solution():
    """
    Solution to Project Euler problem 30
    https://projecteuler.net/problem=30

    Find the sum of all the numbers that can be written as the sum of fifth
    powers of their digits.
    """
    print(sum_of_num_equal_to_sum_of_powers_of_digits(power=5))


def test_solution():
    assert sum_of_num_equal_to_sum_of_powers_of_digits(power=4) == 19_316
    assert sum_of_num_equal_to_sum_of_powers_of_digits(power=5) == 443_839


def sum_of_num_equal_to_sum_of_powers_of_digits(power: int) -> int:
    num_sum = 0

    # For any number n with k digits, the maximum powers of its digits is
    # k * 9**power.
    max_digit_power = 9**power
    k = 1
    while k <= num_of_digits(k * max_digit_power):
        k += 1
    max_num = (k - 1) * max_digit_power

    for n in range(10, max_num + 1):
        sum_digit_power = 0
        head = n
        while head > 0:
            digit = head % 10
            sum_digit_power += digit**power
            head //= 10
        if sum_digit_power == n:
            num_sum += n

    return num_sum

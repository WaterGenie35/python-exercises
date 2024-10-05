def solution():
    """
    Solution to Project Euler problem 48
    https://projecteuler.net/problem=48

    Find the last 10 digits of the series 1^1 + 2^2 + 3^3 + ... + 1_000^1_000.
    """
    print(last_10_digits_of_sum_of_self_powers_lte(1_000))


def test_solution():
    assert last_10_digits_of_sum_of_self_powers_lte(10) == 405_071_317
    assert last_10_digits_of_sum_of_self_powers_lte(1_000) == 9_110_846_700


def last_10_digits_of_sum_of_self_powers_lte(n: int) -> int:
    sum_num = 0
    for i in range(1, n + 1):
        power = i**i % 10_000_000_000
        sum_num = (sum_num + power) % 10_000_000_000
    return sum_num

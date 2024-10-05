def solution():
    """
    Solution to Project Euler problem 26
    https://projecteuler.net/problem=26

    Find d < 1_000 for which 1/d contains the longest recurring cycle in its
    decimal fraction.
    """
    print(denominator_lt_with_longest_period(1_000))


def test_solution():
    assert denominator_lt_with_longest_period(11) == 7
    assert denominator_lt_with_longest_period(1_000) == 983


def denominator_lt_with_longest_period(max_denominator: int) -> int:
    longest_period = 0
    denominator_of_longest_period = None
    for d in range(1, max_denominator):
        period = period_of_unit_fraction(d)
        if period > longest_period:
            longest_period = period
            denominator_of_longest_period = d
    return denominator_of_longest_period


def period_of_unit_fraction(denominator: int) -> int:
    # https://math.stackexchange.com/a/2442992
    if denominator % 2 == 0:
        return period_of_unit_fraction(denominator // 2)
    if denominator % 5 == 0:
        return period_of_unit_fraction(denominator // 5)

    n = 1
    remainder = 10**n % denominator
    while remainder != 1:
        if remainder == 0:
            return 0
        n += 1
        remainder = 10**n % denominator
    return n

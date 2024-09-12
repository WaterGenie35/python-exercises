def solution():
    """
    Solution to Project Euler problem 97
    https://projecteuler.net/problem=97

    Find the last 10 digits of the prime number (28_433 * 2**7_830_457) + 1.
    """
    print(last_10_digits())


def test_solution():
    assert last_10_digits() == 8_739_992_577


def last_10_digits() -> int:
    return ((28_433 * 2**7_830_457) + 1) % 10**10

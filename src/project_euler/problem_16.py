def solution():
    """
    Solution to Project Euler problem 16
    https://projecteuler.net/problem=16

    Find the sum of the digits of 2^1_000.
    """
    print(sum_of_digits(2**1_000))


def sum_of_digits(number: int) -> int:
    s = 0
    n = number
    while n > 0:
        s += n % 10
        n //= 10
    return s

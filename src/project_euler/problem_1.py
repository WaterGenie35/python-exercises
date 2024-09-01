def solution():
    """
    Solution to Project Euler problem 1
    https://projecteuler.net/problem=1

    Find the sum of all the multiples of 3 or 5 below 1_000.
    """
    print(sum_of_multiples_of_3_or_5_lt(1_000))


def sum_of_multiples_of_3_or_5_lt(max: int) -> int:
    return sum(n for n in range(1, max) if n % 3 == 0 or n % 5 == 0)

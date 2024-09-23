from utils.string import is_palindrome


def solution():
    """
    Solution to Project Euler problem 55
    https://projecteuler.net/problem=55

    Find the number of Lychrel numbers below 10_000.
    Lychrel numbers are positive integers that never forms a palindrome through
    at least 1 application of the following process:
      1. Reverse the digits
      2. Add the number and its reverse
    Assume that a number less than 10_000 can be identified as a Lychrel number
    or otherwise in less than 50 iterations.
    """
    print(num_lychrel_lt(10_000))


def test_solution():
    assert num_lychrel_lt(10_000) == 249


def num_lychrel_lt(upper_bound: int) -> int:
    num_lychrel = 0
    for n in range(upper_bound):
        step = n
        iter = 1
        is_lychrel = True
        while iter < 50:
            reverse = int(str(step)[::-1])
            step += reverse
            if is_palindrome(str(step)):
                is_lychrel = False
                break
            iter += 1
        if is_lychrel:
            num_lychrel += 1
    return num_lychrel

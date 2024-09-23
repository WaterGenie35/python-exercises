from utils.string import is_palindrome


def solution():
    """
    Solution to Project Euler problem 36
    https://projecteuler.net/problem=36

    Find the sum of all numbers less than 1_000_000 that are palindromic in
    base 10 and 2.
    """
    print(num_base_2_and_10_palindromes_lt(1_000_000))


def test_solution():
    assert num_base_2_and_10_palindromes_lt(1_000_000) == 872_187


def num_base_2_and_10_palindromes_lt(upper_bound: int) -> int:
    num_sum = 0
    for n in range(1, upper_bound):
        base_2 = bin(n)[2:]
        base_10 = str(n)
        if is_palindrome(base_2) and is_palindrome(base_10):
            num_sum += n
    return num_sum

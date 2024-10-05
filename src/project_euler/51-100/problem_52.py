from utils.math import is_permutation, num_of_digits


def solution():
    """
    Solution to Project Euler problem 52
    https://projecteuler.net/problem=52

    Find the smallest positive integer x such that x, 2x, 3x, 4x, 5x, and 6x
    contain the same digits.
    """
    print(permuted_multiples(6))


def test_solution():
    assert permuted_multiples(6) == 142_857


def permuted_multiples(max_multiple: int) -> int:
    x = 1
    found = False
    while not found:
        if num_of_digits(x) < num_of_digits(x * max_multiple):
            x += 1
            continue

        permute = True
        for m in range(2, max_multiple + 1):
            if not is_permutation(x, x * m):
                permute = False
                break
        found = permute
        if found:
            break

        x += 1
    return x

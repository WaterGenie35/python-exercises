from utils.math import is_prime


def solution():
    """
    Solution to Project Euler problem 58
    https://projecteuler.net/problem=58
    """
    print(spiral_side_length_with_diagonal_primes_ratio_lt(0.1))


# TODO: optimize
# def test_solution():
#     assert spiral_side_length_with_diagonal_primes_ratio_lt(0.1) == 26_241


def spiral_side_length_with_diagonal_primes_ratio_lt(ratio_lt: float) -> int:
    diagonal_head = 1
    layer = 1
    side_length = 1
    num_primes = 0
    num_diagonals = 1
    ratio = 1
    while not ratio < ratio_lt:
        layer += 1
        side_length = (2 * layer) - 1
        for i in range(4):
            diagonal_head += side_length - 1
            # Can ignore bottom-right diagonals since they are squares
            if i < 3 and is_prime(diagonal_head):
                num_primes += 1
        num_diagonals += 4
        ratio = num_primes / num_diagonals
    return side_length

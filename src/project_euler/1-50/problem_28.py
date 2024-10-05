def solution():
    """
    Solution to Project Euler problem 28
    https://projecteuler.net/problem=28

    Find the sum of numbers on the diagonals in a 1_001 by 1_001 spiral.
    A spiral is formed by starting with 1 and moving clockwise, e.g.
      21 22 23 24 25
      20  7  8  9 10
      19  6  1  2 11
      18  5  4  3 12
      17 16 15 14 13
    """
    print(sum_of_diagonals_in_spiral_with_side_length(1_001))


def test_solution():
    assert sum_of_diagonals_in_spiral_with_side_length(5) == 101
    assert sum_of_diagonals_in_spiral_with_side_length(1_001) == 669_171_001


def sum_of_diagonals_in_spiral_with_side_length(n: int) -> int:
    # Just assuming odd n for now
    # Then a spiral with side length n will have n**2 in the top right corner.
    # And the next spiral with side length n + 2 will have corners:
    #   n**2 + 1*(n + 1)
    #   n**2 + 2*(n + 1)
    #   n**2 + 3*(n + 1)
    #   n**2 + 4*(n + 1)
    if n == 0:
        return 0
    diagonal_sum = 1
    head = 1
    while head < n:
        diagonal_sum += (4 * head**2) + (10 * (head + 1))
        head += 2
    return diagonal_sum

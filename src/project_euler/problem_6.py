def solution():
    """
    Solution to Project Euler problem 6
    https://projecteuler.net/problem=6

    Find the difference between the sum of squares and the square of the sum of
    the first 100 natural numbers.
    """
    print(difference_sum_of_squares_and_square_of_sum_lte(100))


def difference_sum_of_squares_and_square_of_sum_lte(max: int) -> int:
    sum_of_squares = sum(n**2 for n in range(1, max + 1))
    square_of_sum = sum(n for n in range(1, max + 1)) ** 2
    return abs(sum_of_squares - square_of_sum)

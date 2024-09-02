# TODO: optimize
def solution():
    """
    Solution to Project Euler problem 5
    https://projecteuler.net/problem=5

    Find the smallest positive number evenly divisible by 1 to 20.
    """
    print(smallest_number_divisible_lte(20))


def test_solution():
    assert smallest_number_divisible_lte(10) == 2_520
    # assert smallest_number_divisible_lte(20) == 232_792_560


def smallest_number_divisible_lte(max_divisor: int) -> int:
    n = max_divisor

    # Solution exists by stipulation
    while True:
        if divisible_up_to(n, max_divisor):
            return n
        n += max_divisor


def divisible_up_to(n: int, max_divisor: int) -> bool:
    divisor = 1
    while divisor <= max_divisor:
        if n % divisor != 0:
            return False
        divisor += 1
    return True

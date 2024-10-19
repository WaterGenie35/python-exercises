from math import ceil, floor, sqrt


def solution():
    """
    Solution to Project Euler problem 206
    https://projecteuler.net/problem=206
    """
    print(find_concealed_square())


# TODO: optimize
def test_solution():
    assert find_concealed_square() == 1_389_019_170


def find_concealed_square() -> int:
    min_root = floor(sqrt(1020304050607080900))
    max_root = ceil(sqrt(1929394959697989990))
    # Square ends in 0 if root ends in 0
    for root in range(min_root, max_root + 1, 10):
        square = root**2
        # print(f"{root} -> {square}")
        if is_concealed_square(square):
            return root


def is_concealed_square(num: int) -> bool:
    if num % 10 != 0:
        return False

    n = num
    pattern_digit = 9
    while n > 0:
        n //= 100
        digit = n % 10
        if digit != pattern_digit:
            return False
        pattern_digit -= 1

    return True

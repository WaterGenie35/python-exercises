def solution():
    """
    Solution to Project Euler problem 40
    https://projecteuler.net/problem=40

    Let d_n be the nth digit in the irrational decimal fraction created by
    concatenating positive integers in sequence (0.123456789101112131415...).
    Find the product of d_i for i = 1, 10, 100, 1_000, 10_000, 100_000, and
    1_000_000.
    """
    print(product_of_champernowne_constants())


def test_solution():
    assert product_of_champernowne_constants() == 210


def product_of_champernowne_constants() -> int:
    product = 1
    for i in range(0, 7):
        product *= nth_digit_of_positive_integer_decimals(10**i)
    return product


def nth_digit_of_positive_integer_decimals(n: int) -> int:
    # Number of d-digit numbers:
    #   (10^d)-1 - 10^(d-1) + 1
    #   (10^d) - 10^(d-1)
    #   (10 * 10^(d-1)) - 10^(d-1)
    #   9 * 10^(d-1)
    # Number of digits all d-digit numbers has in total:
    #   d * 9 * 10^(d-1)
    counter_digit = 1
    prev_num_counter_digits = 0
    num_counter_digits = 9
    while num_counter_digits < n:
        counter_digit += 1
        prev_num_counter_digits = num_counter_digits
        num_counter_digits += counter_digit * 9 * 10 ** (counter_digit - 1)

    counter_group = 10 ** (counter_digit - 1)
    counter_digit_offset = n - prev_num_counter_digits - 1
    counter_num = counter_group + (counter_digit_offset // counter_digit)
    counter_offset = counter_digit_offset % counter_digit
    reverse_counter_offset = counter_digit - counter_offset - 1
    return (counter_num // 10**reverse_counter_offset) % 10

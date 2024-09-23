from utils.math import is_prime


def solution():
    """
    Solution to Project Euler problem 27
    https://projecteuler.net/problem=27

    Find the product of coefficients a and b for the quadratic expression
    n**2 + an + b that produces the maximum number of primes for consecutive
    value of n starting with n = 0, |a| < 1_000 and |b| < 1_000.
    """
    print(product_of_quadratic_coefficient_with_max_consecutive_primes(1_000))


def test_solution():
    assert product_of_quadratic_coefficient_with_max_consecutive_primes(1_000) == -59_231


def product_of_quadratic_coefficient_with_max_consecutive_primes(abs_coeff_lt: int) -> int:
    # Note for n = 0, n**2 + (a * n) + b = b, so we only need to consider prime b's.
    product_of_max = None
    greatest_num_consecutive_primes = 0
    for a in range(-abs_coeff_lt + 1, abs_coeff_lt):
        for b in range(3, abs_coeff_lt):
            if not is_prime(b):
                b += 2
                continue
            n = 0
            num_consecutive_primes = 0
            head = n**2 + (a * n) + b
            while is_prime(head):
                num_consecutive_primes += 1
                n += 1
                head = n**2 + (a * n) + b
            if num_consecutive_primes > greatest_num_consecutive_primes:
                greatest_num_consecutive_primes = num_consecutive_primes
                product_of_max = a * b
            b += 1
        a += 1
    return product_of_max

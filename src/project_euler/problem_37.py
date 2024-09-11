from utils.math import generate_primes, num_of_digits


def solution():
    """
    Solution to Project Euler problem 37
    https://projecteuler.net/problem=37

    Find the sum of the first 11 primes that are both truncatable from
    left to right and from right to left.
    (Assume there are only 11 such primes)
    A prime number is truncatable from left to right if the numbers generated
    from removing digits from left to right are all primes. Similarly for
    right to left.
    """
    print(sum_of_truncatable_primes())


def test_solution():
    assert sum_of_truncatable_primes() == 748_317


# TODO: possibly start with (limited?) right to left truncatables?
def sum_of_truncatable_primes():
    truncatable_sum = 0
    count = 0
    primes = set()
    for prime in generate_primes():
        primes.add(prime)
        if prime < 10:
            continue

        truncatable = True

        left_to_right = prime
        num_digits = num_of_digits(prime)
        while num_digits > 1:
            left_to_right %= 10 ** (num_digits - 1)
            # Can't -=1 since we may skip 0 digits
            num_digits = num_of_digits(left_to_right)
            if left_to_right not in primes:
                truncatable = False
                break
        if not truncatable:
            continue

        right_to_left = prime
        num_digits = num_of_digits(prime)
        while num_digits > 1:
            right_to_left //= 10
            num_digits -= 1
            if right_to_left not in primes:
                truncatable = False
                break
        if not truncatable:
            continue

        count += 1
        truncatable_sum += prime
        if count == 11:
            break
    return truncatable_sum

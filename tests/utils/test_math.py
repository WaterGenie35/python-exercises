from project_euler.problem_16 import sum_of_digits
from utils.math import (
    choose,
    factors_of,
    greatest_common_factor,
    is_amicable,
    is_permutation,
    is_prime,
    nth_prime,
    num_factors,
    num_of_digits,
    primes_lte,
)


def test_is_prime():
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(65_537)
    assert is_prime(87_178_291_199)
    # assert is_prime(3_331_113_965_338_635_107)

    assert not is_prime(-3)
    assert not is_prime(0)
    assert not is_prime(1)
    assert not is_prime(4)
    assert not is_prime(65_535)
    assert not is_prime(87_178_291_197)
    # assert not is_prime(3_331_113_965_338_635_109)


def test_nth_prime():
    assert nth_prime(1) == 2
    assert nth_prime(2) == 3
    assert nth_prime(283) == 1_847
    # assert nth_prime(503_921) == 7_430_947


def test_primes_lte():
    assert primes_lte(1) == []
    assert primes_lte(2) == [2]
    assert primes_lte(10) == [2, 3, 5, 7]
    assert primes_lte(11) == [2, 3, 5, 7, 11]
    assert primes_lte(75) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]


def test_factors_of():
    assert factors_of(1) == [1]
    assert factors_of(28) == [1, 2, 4, 7, 14, 28]
    assert factors_of(33_907_329) == [
        1,
        3,
        9,
        27,
        81,
        647,
        1_941,
        5_823,
        17_469,
        52_407,
        418_609,
        1_255_827,
        3_767_481,
        11_302_443,
        33_907_329,
    ]


def test_num_factors():
    assert num_factors(1) == 1
    assert num_factors(28) == 6
    assert num_factors(33_907_329) == 15
    assert num_factors(76_576_500) == 576


def test_greatest_common_factors():
    assert greatest_common_factor(0, 0) == 0
    assert greatest_common_factor(3_293_092, 0) == 3_293_092
    assert greatest_common_factor(48, 18) == 6
    assert greatest_common_factor(42, 56) == 14


def test_is_amicable():
    assert is_amicable(220)
    assert is_amicable(284)

    assert not is_amicable(1)
    assert not is_amicable(6)


def test_choose():
    assert choose(1, 1) == 1
    assert choose(4, 2) == 6
    assert choose(235, 1) == 235
    assert choose(35, 17) == 4_537_567_650


def test_num_of_digits():
    assert num_of_digits(0) == 1
    assert num_of_digits(9) == 1
    assert num_of_digits(123_456) == 6
    assert num_of_digits(-9_004) == 4


def test_sum_of_digits():
    assert sum_of_digits(0) == 0
    assert sum_of_digits(6) == 6
    assert sum_of_digits(1_023_009) == 15


def test_is_permutation():
    assert is_permutation(1487, 4817)
    assert is_permutation(10013, 11300)

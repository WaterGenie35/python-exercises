from utils.math import choose, divisors_of, is_prime, nth_prime, primes_lte


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


def test_divisors_of():
    assert divisors_of(1) == [1]
    assert divisors_of(28) == [1, 2, 4, 7, 14, 28]
    assert divisors_of(33_907_329) == [
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


def test_choose():
    assert choose(1, 1) == 1
    assert choose(4, 2) == 6
    assert choose(235, 1) == 235
    assert choose(35, 17) == 4_537_567_650

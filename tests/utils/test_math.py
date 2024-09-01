from utils.math import is_prime, nth_prime


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

from utils.string import is_palindrome


def test_is_palindrome():
    assert is_palindrome("racecar")
    assert is_palindrome("1830110381")
    assert is_palindrome("foo 123 321 oof")

    assert not is_palindrome("racecars")
    assert not is_palindrome("12345678")
    assert not is_palindrome("foo 123 321 bar")

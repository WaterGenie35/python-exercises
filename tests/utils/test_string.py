from utils.string import characters_frequency, humanize_number, is_palindrome


def test_is_palindrome():
    assert is_palindrome("racecar")
    assert is_palindrome("1830110381")
    assert is_palindrome("foo 123 321 oof")

    assert not is_palindrome("racecars")
    assert not is_palindrome("12345678")
    assert not is_palindrome("foo 123 321 bar")


def test_humanize_number():
    assert humanize_number(0) == "zero"
    assert humanize_number(2) == "two"
    assert humanize_number(13) == "thirteen"
    assert humanize_number(45) == "forty-five"
    assert humanize_number(678) == "six hundred and seventy-eight"
    assert humanize_number(9_001) == "nine thousand and one"
    # The "and" in 209 is just separating the hundredth and remaining digits
    # and doesn't affect the "and" separating every 1_000 powers.
    assert humanize_number(209_001) == "two hundred and nine thousand and one"
    assert humanize_number(12_003_405) == "twelve million, three thousand, and four hundred and five"
    assert humanize_number(102_000_034_000) == "one hundred and two billion and thirty-four thousand"
    # Test overflow (powers step up to "million")
    short_powers_step = {3: "thousand", 6: "million"}
    assert humanize_number(2_000_000_000, short_powers_step) == "two thousand million"
    assert humanize_number(3_000_000_000_050, short_powers_step) == "three million million and fifty"
    assert humanize_number(3_000_020_000_050, short_powers_step) == "three million and twenty million and fifty"
    # Not quite clear on how repeated overflow works in English, arbitrary for now by just using recursive calls
    # Change this as we decide on the usage
    assert humanize_number(3_140_020_017_050, short_powers_step) == (
        "three million, one hundred and forty thousand, and twenty million, seventeen thousand, and fifty"
    )


def test_characters_frequency():
    assert characters_frequency("") == {}
    assert characters_frequency("foo") == {"f": 1, "o": 2}
    assert characters_frequency("foo bar baz") == {"f": 1, "o": 2, " ": 2, "b": 2, "a": 2, "r": 1, "z": 1}

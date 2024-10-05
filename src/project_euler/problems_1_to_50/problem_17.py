from utils.string import humanize_number


def solution():
    """
    Solution to Project Euler problem 17
    https://projecteuler.net/problem=17

    Find the number of letters used if numbers from 1 to 1_000 inclusive were
    written out in words.
    Ignore non-numeral characters.
    Use "and" as in British English:
    https://en.wikipedia.org/wiki/English_numerals#Cardinal_numbers
    """
    print(num_letters_of_humanized_numbers_lte(1_000))


def test_solution():
    assert num_letters_of_humanized_numbers_lte(5) == 19
    assert num_letters_of_humanized_numbers_lte(1_000) == 21_124


def num_letters_of_humanized_numbers_lte(n: int) -> int:
    num_letters = 0

    for i in range(1, n + 1):
        humanized = humanize_number(i)
        num_letters += len(strip(humanized))

    return num_letters


def strip(humanized_number: str) -> str:
    stripped = humanized_number.replace(",", "")
    stripped = stripped.replace("-", "")
    stripped = stripped.replace(" ", "")
    return stripped

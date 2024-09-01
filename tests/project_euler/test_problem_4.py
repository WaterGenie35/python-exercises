from project_euler.problem_4 import largest_palindrome_product_from_digits


def test_solution():
    assert largest_palindrome_product_from_digits(2) == 9009
    assert largest_palindrome_product_from_digits(3) == 906609

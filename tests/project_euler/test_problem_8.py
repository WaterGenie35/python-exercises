from project_euler.problem_8 import NUM_REPR, greatest_product_of_consecutive_digits


def test_solution():
    assert greatest_product_of_consecutive_digits(NUM_REPR, 4) == 5_832
    assert greatest_product_of_consecutive_digits(NUM_REPR, 13) == 23_514_624_000

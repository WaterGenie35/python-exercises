from project_euler.problem_6 import difference_sum_of_squares_and_square_of_sum_lte


def test_solution():
    assert difference_sum_of_squares_and_square_of_sum_lte(10) == 2_640
    assert difference_sum_of_squares_and_square_of_sum_lte(100) == 25_164_150

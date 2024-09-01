from project_euler.problem_13 import NUMS, first_n_digits_of_sum


def test_solution():
    assert first_n_digits_of_sum(NUMS, 10) == [5, 5, 3, 7, 3, 7, 6, 2, 3, 0]

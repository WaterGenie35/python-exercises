from project_euler.problem_16 import sum_of_digits


def test_solution():
    assert sum_of_digits(2**1_000) == 1_366

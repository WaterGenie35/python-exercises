from project_euler.problem_1 import sum_of_multiples_of_3_or_5_lt


def test_solution():
    assert sum_of_multiples_of_3_or_5_lt(10) == 23
    assert sum_of_multiples_of_3_or_5_lt(1_000) == 233_168

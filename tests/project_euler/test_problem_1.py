from project_euler.problem_1 import sum_of_multiples_of_3_or_5_below


def test_solution():
    assert sum_of_multiples_of_3_or_5_below(10) == 23
    assert sum_of_multiples_of_3_or_5_below(1_000) == 233_168

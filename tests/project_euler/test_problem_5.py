from project_euler.problem_5 import smallest_number_divisible_lte


def test_solution():
    assert smallest_number_divisible_lte(10) == 2_520
    assert smallest_number_divisible_lte(20) == 232_792_560

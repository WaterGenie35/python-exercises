from project_euler.problem_12 import first_triangle_number_with_num_divisors_gt


def test_solution():
    assert first_triangle_number_with_num_divisors_gt(5) == 28
    assert first_triangle_number_with_num_divisors_gt(500) == 76_576_500

from project_euler.problem_2 import sum_of_even_fibonacci_lt


def test_solution():
    assert sum_of_even_fibonacci_lt(4_000_000) == 4_613_730

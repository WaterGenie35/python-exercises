from project_euler.problem_9 import product_of_pythagorean_with_triplet_sum


def test_solution():
    assert product_of_pythagorean_with_triplet_sum(1_000) == 31_875_000

from project_euler.problem_3 import largest_prime_factor_of


def test_solution():
    assert largest_prime_factor_of(13_195) == 29
    assert largest_prime_factor_of(600_851_475_143) == 6_857

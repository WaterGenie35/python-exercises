from project_euler.problem_10 import sum_of_primes_lt


def test_solution():
    assert sum_of_primes_lt(10) == 17
    assert sum_of_primes_lt(2_000_000) == 142_913_828_922

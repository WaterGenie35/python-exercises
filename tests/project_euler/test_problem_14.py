from project_euler.problem_14 import longest_chain_length_with_starting_num_lt


def test_solution():
    assert longest_chain_length_with_starting_num_lt(1_000_000) == 837_799

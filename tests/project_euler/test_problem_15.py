from project_euler.problem_15 import num_lattice_paths


def test_solution():
    assert num_lattice_paths(2, 2) == 6
    assert num_lattice_paths(20, 20) == 137_846_528_820

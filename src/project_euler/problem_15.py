from utils.math import choose


def solution():
    """
    Solution to Project Euler problem 15
    https://projecteuler.net/problem=15

    Find the number of lattice paths through a 20 x 20 grid.
    A lattice path starts from the top left corner of a grid to the bottom
    right corner by only moving right or down.
    """
    print(num_lattice_paths(20, 20))


def test_solution():
    assert num_lattice_paths(2, 2) == 6
    assert num_lattice_paths(20, 20) == 137_846_528_820


def num_lattice_paths(width: int, height: int) -> int:
    # There are width + height times in which we must pick between moving
    # right or down.
    # We must have width right moves (forcing height down moves and vice versa).
    return choose(width + height, min(width, height))

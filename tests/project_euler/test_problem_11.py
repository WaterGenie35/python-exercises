from project_euler.problem_11 import GRID, greatest_product_of_adjacent_numbers


def test_solution():
    assert greatest_product_of_adjacent_numbers(GRID, 4) == 70_600_674

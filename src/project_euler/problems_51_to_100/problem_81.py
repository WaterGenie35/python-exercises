import os
from typing import List


def solution():
    """
    Solution to Project Euler problem 81
    https://projecteuler.net/problem=81

    Find the minimal lattice path sum through the given grid.
    A lattice path starts from the top left corner of a grid to the bottom
    right corner by only moving right or down.
    """
    print(min_lattice_path_sum(parse_grid("problem_81_grid.txt")))


def test_solution():
    assert (
        min_lattice_path_sum(
            [
                [131, 673, 234, 103, 18],
                [201, 96, 342, 965, 150],
                [630, 803, 746, 422, 111],
                [537, 699, 497, 121, 956],
                [805, 732, 524, 37, 331],
            ]
        )
        == 2_427
    )
    assert min_lattice_path_sum(parse_grid("problem_81_grid.txt")) == 427_337


def parse_grid(filename: str) -> List[List[int]]:
    grid = []
    current_dir = os.path.dirname(__file__)
    filepath = os.path.join(current_dir, filename)
    with open(filepath) as file:
        for line in file:
            grid.append([int(i) for i in line.strip().split(",")])
    return grid


def min_lattice_path_sum(grid: List[List[int]]) -> int:
    if len(grid) == 0:
        return None
    if len(grid[0]) == 0:
        return None

    width = len(grid[0])
    height = len(grid)
    min_grid = [[0] * width] * height
    for i in range(height - 1, -1, -1):
        for j in range(width - 1, -1, -1):
            bottom_edge = i == height - 1
            right_edge = j == width - 1
            down_path = min_grid[i + 1][j] if i < height - 1 else None
            right_path = min_grid[i][j + 1] if j < width - 1 else None
            cell = grid[i][j]

            if bottom_edge and right_edge:
                min_grid[i][j] = cell
            elif bottom_edge:
                min_grid[i][j] = cell + right_path
            elif right_edge:
                min_grid[i][j] = cell + down_path
            else:
                min_grid[i][j] = cell + min(down_path, right_path)
    return min_grid[0][0]

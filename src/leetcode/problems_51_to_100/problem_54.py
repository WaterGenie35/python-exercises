from math import ceil
from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    """
    Solution to LeetCode problem 54
    https://neetcode.io/problems/spiral-matrix
    https://leetcode.com/problems/spiral-matrix/
    """
    height = len(matrix)
    width = len(matrix[0])

    # Implement ceil manually for submission instead of using import
    ring_count = ceil(min(width, height) / 2)
    ring_width = width
    ring_height = height

    spiral = []
    for ring in range(ring_count):
        ring_width = width - (2 * ring)
        ring_height = height - (2 * ring)

        row = ring
        col = ring
        for top_index in range(ring_width):
            spiral.append(matrix[row][col + top_index])

        if ring_height > 1:
            row = ring + 1
            col = ring + ring_width - 1
            for right_index in range(ring_height - 1):
                spiral.append(matrix[row + right_index][col])

            if ring_width > 1:
                row = ring + ring_height - 1
                col = ring + ring_width - 2
                for bottom_index in range(ring_width - 1):
                    spiral.append(matrix[row][col - bottom_index])

                row = ring + ring_height - 2
                col = ring
                for left_index in range(ring_height - 2):
                    spiral.append(matrix[row - left_index][col])

    return spiral


def test_solution():
    assert spiral_order([[]]) == []
    assert spiral_order([[1, 2, 3, 4]]) == [1, 2, 3, 4]
    assert spiral_order([[1], [2], [3], [4]]) == [1, 2, 3, 4]
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

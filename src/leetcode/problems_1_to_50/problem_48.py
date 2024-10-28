from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Solution to LeetCode problem 48
    https://neetcode.io/problems/rotate-matrix
    https://leetcode.com/problems/rotate-image/
    """
    # Map coordinate to its rotated position,
    # Continue mapping the one that will get replaced, forming a cycle of 4
    # positions.
    # Each ring of width k has k-1 such cycles.
    # Matrix of width (or height) n will have ceil(n/2) rings we have to rotate.
    side_length = len(matrix)
    num_rings = side_length // 2
    for ring in range(num_rings):
        ring_width = side_length - (2 * ring)
        for cycle in range(ring_width - 1):
            row = ring
            col = ring + cycle
            head_1 = matrix[row][col]

            row = col
            col = ring + ring_width - 1
            head_2 = matrix[row][col]
            matrix[row][col] = head_1

            row = col
            col = ring + ring_width - cycle - 1
            head_3 = matrix[row][col]
            matrix[row][col] = head_2

            row = col
            col = ring
            head_4 = matrix[row][col]
            matrix[row][col] = head_3

            row = col
            col = ring + cycle
            matrix[row][col] = head_4


def test_solution():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

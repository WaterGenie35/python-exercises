from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    """
    Solution to LeetCode problem 74
    https://neetcode.io/problems/search-2d-matrix
    https://leetcode.com/problems/search-a-2d-matrix/
    """
    height = len(matrix)
    width = len(matrix[0])
    size = width * height

    head = 0
    tail = size - 1
    while head < tail - 1:
        mid = (head + tail) // 2
        matrix_mid = matrix[mid // width][mid % width]
        if matrix_mid == target:
            return True
        if matrix_mid < target:
            head = mid
        else:
            tail = mid
    matrix_head = matrix[head // width][head % width]
    matrix_tail = matrix[tail // width][tail % width]
    return matrix_head == target or matrix_tail == target


def test_solution():
    assert search_matrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10)
    assert not search_matrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 15)

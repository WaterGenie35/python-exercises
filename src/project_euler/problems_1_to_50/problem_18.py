from typing import List

TRIANGLE = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
]


def solution():
    """
    Solution to Project Euler problem 18
    https://projecteuler.net/problem=18

    Find the maximum total path from top to bottom of the given triangle.

    Define a triangle t of height n to be a List[List[int]] of length n
    where the length of t[k] is k+1.
    Define a path from top to bottom of a triangle t to be a list of n elements
    p_0 to p_n-1 such that:
        - p_k is in t[k], and i_k be the index of p_k in t[k]
        - p_0 is t[0][0] (i_0 = 0)
        - p_k+1 is either t[k][i_k] or t[k][i_k - 1]
    """
    print(max_path_in_triangle(TRIANGLE))


def test_solution():
    assert (
        max_path_in_triangle(
            [
                [3],
                [7, 4],
                [2, 4, 6],
                [8, 5, 9, 3],
            ]
        )
        == 23
    )
    assert max_path_in_triangle(TRIANGLE) == 1_074


def max_path_in_triangle(triangle: List[List[int]]) -> int:
    if len(triangle) == 0 or len(triangle[0]) == 0:
        return None

    running_max = []
    running_max.append([triangle[0][0]])
    for row in range(1, len(triangle)):
        running_max.append([])
        for head in range(0, len(triangle[row])):
            next_element = triangle[row][head]
            prev_left = running_max[row - 1][head - 1] if head > 0 else float('-inf')
            prev_right = running_max[row - 1][head] if head < len(triangle[row]) - 1 else float('-inf')
            running_max[row].append(max(prev_left, prev_right) + next_element)
    return max(running_max[-1])

import os
from typing import List

from project_euler.problem_18 import max_path_in_triangle


def solution():
    """
    Solution to Project Euler problem 67
    https://projecteuler.net/problem=67

    Find the maximum total path from top to bottom of the given triangle.

    Define a triangle t of height n to be a List[List[int]] of length n
    where the length of t[k] is k+1.
    Define a path from top to bottom of a triangle t to be a list of n elements
    p_0 to p_n-1 such that:
        - p_k is in t[k], and i_k be the index of p_k in t[k]
        - p_0 is t[0][0] (i_0 = 0)
        - p_k+1 is either t[k][i_k] or t[k][i_k - 1]
    """
    print(max_path_in_triangle(parse_triangle("problem_67_triangle.txt")))


def test_solution():
    assert max_path_in_triangle(parse_triangle("problem_67_triangle.txt")) == 7_273


def parse_triangle(filename: str) -> List[List[int]]:
    triangle = []
    current_dir = os.path.dirname(__file__)
    filepath = os.path.join(current_dir, filename)
    with open(filepath) as file:
        for line in file:
            triangle.append([int(i) for i in line.split()])
    return triangle

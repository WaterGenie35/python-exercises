import math
from typing import List

from utils.math import is_permutation


def solution():
    """
    Solution to Project Euler problem 62
    https://projecteuler.net/problem=62
    """
    print(smallest_cube_with_n_number_of_cube_permutations(n=5))


# TODO: optimize
def test_solution():
    assert smallest_cube_with_n_number_of_cube_permutations(n=3) == 41_063_625
    # assert smallest_cube_with_n_number_of_cube_permutations(n=5) == 127_035_954_683


def smallest_cube_with_n_number_of_cube_permutations(n: int) -> int:
    digits = 1
    while True:
        same_digit_cubes = cubes_with_n_digits(digits)
        examined_cubes = set()
        for i, cube in enumerate(same_digit_cubes):
            if cube in examined_cubes:
                continue
            num_cube_permutations = 1
            same_group = [cube]
            for j in range(i + 1, len(same_digit_cubes)):
                other_cube = same_digit_cubes[j]
                if other_cube in examined_cubes:
                    continue
                if is_permutation(cube, other_cube):
                    num_cube_permutations += 1
                    same_group.append(other_cube)
            if num_cube_permutations == n:
                return cube
            for c in same_group:
                examined_cubes.add(c)

        digits += 1


def cubes_with_n_digits(n: int) -> List[int]:
    start = math.ceil((10 ** (n - 1)) ** (1 / 3))
    end = math.floor((10**n) ** (1 / 3))
    return [i**3 for i in range(start, end + 1)]

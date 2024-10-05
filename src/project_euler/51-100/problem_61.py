from typing import Callable, Dict, List

from utils.search import binary_search


def solution():
    """
    Solution to Project Euler problem 61
    https://projecteuler.net/problem=61
    """
    print(sum_of_6_cyclic_4_digit_polygonal_numbers())


def test_solution():
    assert sum_of_6_cyclic_4_digit_polygonal_numbers() == 28_684


def sum_of_6_cyclic_4_digit_polygonal_numbers() -> int:
    triangles = four_digit_polygonal_numbers(lambda n: n * (n + 1) // 2)
    squares = four_digit_polygonal_numbers(lambda n: n**2)
    pentagonals = four_digit_polygonal_numbers(lambda n: n * ((3 * n) - 1) // 2)
    hexagonals = four_digit_polygonal_numbers(lambda n: n * ((2 * n) - 1))
    heptagonals = four_digit_polygonal_numbers(lambda n: n * ((5 * n) - 3) // 2)
    octagonals = four_digit_polygonal_numbers(lambda n: n * ((3 * n) - 2))

    all_polygonal_numbers = sorted(set(triangles + squares + pentagonals + hexagonals + heptagonals + octagonals))

    def num_sides(p: int) -> List[str]:
        sides = []
        if binary_search(triangles, p) is not None:
            sides.append('triangles')
        if binary_search(squares, p) is not None:
            sides.append('squares')
        if binary_search(pentagonals, p) is not None:
            sides.append('pentagonals')
        if binary_search(hexagonals, p) is not None:
            sides.append('hexagonals')
        if binary_search(heptagonals, p) is not None:
            sides.append('heptagonals')
        if binary_search(octagonals, p) is not None:
            sides.append('octagonals')
        return sides

    polygonal_tally = {}
    found = False
    nums = []
    for p1 in all_polygonal_numbers:
        nums = [p1]

        for p2 in all_polygonal_numbers:
            if p2 in nums or not is_cyclic(p1, p2):
                continue
            nums = [p1, p2]

            for p3 in all_polygonal_numbers:
                if p3 in nums or not is_cyclic(p2, p3):
                    continue
                nums = [p1, p2, p3]

                for p4 in all_polygonal_numbers:
                    if p4 in nums or not is_cyclic(p3, p4):
                        continue
                    nums = [p1, p2, p3, p4]

                    for p5 in all_polygonal_numbers:
                        if p5 in nums or not is_cyclic(p4, p5):
                            continue
                        nums = [p1, p2, p3, p4, p5]

                        for p6 in all_polygonal_numbers:
                            if p6 in nums or not is_cyclic(p5, p6) or not is_cyclic(p6, p1):
                                continue
                            nums = [p1, p2, p3, p4, p5, p6]

                            polygonal_tally = {
                                'triangles': [],
                                'squares': [],
                                'pentagonals': [],
                                'hexagonals': [],
                                'heptagonals': [],
                                'octagonals': [],
                            }
                            for side in num_sides(p1):
                                polygonal_tally[side].append(p1)
                            for side in num_sides(p2):
                                polygonal_tally[side].append(p2)
                            for side in num_sides(p3):
                                polygonal_tally[side].append(p3)
                            for side in num_sides(p4):
                                polygonal_tally[side].append(p4)
                            for side in num_sides(p5):
                                polygonal_tally[side].append(p5)
                            for side in num_sides(p6):
                                polygonal_tally[side].append(p6)

                            if is_all_sides_representable_by_different_number(polygonal_tally):
                                found = True
                                break
                        if found:  # p5 level
                            break
                    if found:  # p4 level
                        break
                if found:  # p3 level
                    break
            if found:  # p2 level
                break
        if found:  # p1 level
            break
    return sum(nums)


def four_digit_polygonal_numbers(formula: Callable[[int], int]) -> List[int]:
    polygonal_numbers = []
    i = 1
    head = 1
    while head < 10_000:
        head = formula(i)
        if head >= 1_000 and head < 10_000:
            polygonal_numbers.append(head)
        i += 1
    return polygonal_numbers


def is_cyclic(n1: int, n2: int) -> bool:
    return (n1 % 100) == (n2 // 100)


def is_all_sides_representable_by_different_number(tally: Dict[str, List[int]]) -> bool:
    unique_numbers = set()
    for numbers in tally.values():
        if len(numbers) == 0:
            return False
        for n in numbers:
            unique_numbers.add(n)
    if len(unique_numbers) != 6:
        return False

    # TODO: find proper mapping
    # this 1-level deep is just sufficient for this problem but incorrect in general
    for side, numbers in tally.items():
        if len(numbers) > 1:
            continue
        for other_sides, other_numbers in tally.items():
            if side == other_sides:
                continue
            if numbers[0] in other_numbers and len(other_numbers) == 1:
                return False
    return True

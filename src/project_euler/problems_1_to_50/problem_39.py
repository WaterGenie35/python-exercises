def solution():
    """
    Solution to Project Euler problem 39
    https://projecteuler.net/problem=39

    Find p <= 1_000 with maximum number of solutions to p = a + b + c,
    a^2 + b^2 = c^2, for positive integers a, b, and c.
    """
    print(right_angle_triangle_perimeter_lte_with_max_solutions(1_000))


def test_solution():
    assert right_angle_triangle_perimeter_lte_with_max_solutions(1_000) == 840


def right_angle_triangle_perimeter_lte_with_max_solutions(upper_bound: int) -> int:
    max_solutions = 0
    perimeter_of_max_solution = None
    for p in range(3, upper_bound + 1):
        solutions = 0
        for a in range(1, p - 1):
            # c = p - a - b, so a**2 + b**2 = (p - a - b)**2
            # a**2 + b**2 = p**2 -2ap -2bp + a**2 +2ab + b**2
            # Rearrange for b:
            b = (p**2 - (2 * a * p)) // (2 * (p - a))
            c = p - a - b
            if a**2 + b**2 == c**2:
                solutions += 1
        if solutions > max_solutions:
            max_solutions = solutions
            perimeter_of_max_solution = p

    return perimeter_of_max_solution

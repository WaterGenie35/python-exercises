def solution():
    """
    Solution to Project Euler problem 85
    https://projecteuler.net/problem=85
    """
    print(grid_area_with_num_sub_rectangles_closest_to_n(2_000_000))


def test_solution():
    assert grid_area_with_num_sub_rectangles_closest_to_n(2_000_000) == 2_772


def grid_area_with_num_sub_rectangles_closest_to_n(n: int) -> int:
    closest_area = None
    smallest_distance_to_n = float('inf')

    width = 1
    height = 1
    too_large = False
    while not too_large:
        area = width * height
        sub_rectangle_count = num_sub_rectangles(width, height)
        if sub_rectangle_count == n:
            return area

        distance_to_n = abs(n - sub_rectangle_count)

        if height > n or (width == 1 and distance_to_n >= smallest_distance_to_n and sub_rectangle_count > n):
            too_large = True

        # WLOG we consider just rectangles where width <= height
        # Can also skip to next height when we've already exceeded the closest
        # number of sub rectangles since it increases monotonically
        if width == height or (distance_to_n >= smallest_distance_to_n and sub_rectangle_count > n):
            width = 1
            height += 1
        else:
            width += 1

        if distance_to_n < smallest_distance_to_n:
            smallest_distance_to_n = distance_to_n
            closest_area = area

    return closest_area


def num_sub_rectangles(width: int, height: int) -> int:
    # Horizontal: width + 1 choose 2
    # Vertical: height + 1 choose 2
    return (1 / 4) * width * (width + 1) * height * (height + 1)

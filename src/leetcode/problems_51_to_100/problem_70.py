def climb_stairs(n: int) -> int:
    """
    Solution to LeetCode problem 70
    https://neetcode.io/problems/climbing-stairs
    https://leetcode.com/problems/climbing-stairs/

    Given n steps and step size of 1 or 2,
    find the number of ways to climb exactly n steps.
    """
    ways = {1: 1, 2: 2}
    head = 3
    while n not in ways:
        ways[head] = ways[head - 1] + ways[head - 2]
        head += 1
    return ways[n]


def test_solution():
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(4) == 5

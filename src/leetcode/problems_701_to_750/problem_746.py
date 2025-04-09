from typing import List


def min_cost_climbing_stairs(cost: List[int]) -> int:
    """
    Solution to LeetCode problem 746
    https://neetcode.io/problems/min-cost-climbing-stairs
    https://leetcode.com/problems/min-cost-climbing-stairs/

    Given an array where the ith element is the cost of the ith step on the stair,
    find the minimum cost of climbing the stair where we can start on either the
    0th or 1st step, and can take 1 or 2 steps at a time.
    """
    if len(cost) == 1:
        return cost[0]

    ways = {0: cost[-1], 1: cost[-2]}
    num_steps = len(cost)
    head = 2
    while head < num_steps:
        head_cost = cost[num_steps - head - 1]
        ways[head] = head_cost + min(ways[head - 1], ways[head - 2])
        head += 1
    return min(ways[num_steps - 1], ways[num_steps - 2])


def test_solution():
    assert min_cost_climbing_stairs([0, 0, 1, 1]) == 1
    assert min_cost_climbing_stairs([1, 2, 1, 2, 1, 1, 1]) == 4
    assert min_cost_climbing_stairs([10, 15, 20]) == 15
    assert min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6

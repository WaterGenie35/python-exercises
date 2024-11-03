from typing import List


def missing_number(nums: List[int]) -> int:
    """
    Solution to LeetCode problem 268
    https://neetcode.io/problems/missing-number
    https://leetcode.com/problems/missing-number/
    """
    remaining = 0
    for i, num in enumerate(nums):
        remaining ^= i + 1
        remaining ^= num
    return remaining


def test_solution():
    assert missing_number([0]) == 1
    assert missing_number([3, 0, 1]) == 2
    assert missing_number([0, 1]) == 2
    assert missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8

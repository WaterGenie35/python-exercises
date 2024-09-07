from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """
    Solution to LeetCode problem 217
    https://neetcode.io/problems/duplicate-integer
    https://leetcode.com/problems/contains-duplicate/

    Given integer array nums, check if nums contains any duplicates.
    """
    appearances = set()
    for num in nums:
        if num in appearances:
            return True
        appearances.add(num)
    return False


def test_solution():
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])

    assert not contains_duplicate([])
    assert not contains_duplicate([1, 2, 3, 4, -1])

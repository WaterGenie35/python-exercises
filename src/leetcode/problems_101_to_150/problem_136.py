from typing import List


def single_number(nums: List[int]) -> int:
    """
    Solution to LeetCode problem 136
    https://neetcode.io/problems/single-number
    https://leetcode.com/problems/single-number/
    """
    nums_xor = nums[0]
    for num in nums[1:]:
        nums_xor ^= num
    return nums_xor


def test_solution():
    assert single_number([2, 2, 1]) == 1
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert single_number([1]) == 1

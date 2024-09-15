from typing import List


def search(nums: List[int], target: int) -> int:
    """
    Solution to LeetCode problem 704
    https://neetcode.io/problems/binary-search
    https://leetcode.com/problems/binary-search/

    Given an array of integers nums sorted in ascending order, and an integer
    target, search for target in nums. If target exists, then return its index.
    Otherwise, return -1.
    """
    # See utils/search.py
    if len(nums) == 0:
        return -1

    head = 0
    tail = len(nums) - 1
    while head < tail - 1:
        mid = (head + tail) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            head = mid
        else:
            tail = mid

    if nums[head] == target:
        return head
    if nums[tail] == target:
        return tail
    return -1


def test_solution():
    assert search([-1, 0, 2, 4, 6, 8], 4) == 3
    assert search([-1, 0, 2, 4, 6, 8], 3) == -1

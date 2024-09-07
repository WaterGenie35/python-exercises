from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Solution to LeetCode problem 1
    https://neetcode.io/problems/two-integer-sum
    https://leetcode.com/problems/two-sum/

    Given an array of integers nums and an integer target, return the indices
    i != j such that nums[i] + nums[j] == target.
    Assume that there is always a unique solution.
    Sort the solution with smaller index first.
    """
    complement_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in complement_index:
            # Store first two minimum indices
            if len(complement_index[complement]) == 1:
                complement_index[complement].append(i)
            continue
        complement_index[complement] = [i]

    print(complement_index)
    for i, num in enumerate(nums):
        if num in complement_index:
            j = complement_index[num][0]
            if i == j:
                if len(complement_index[num]) == 1:
                    continue
                # Exists by stipulation
                j = complement_index[num][1]
            return [min(i, j), max(i, j)]


def test_solution():
    assert two_sum([3, 4, 5, 6], 7) == [0, 1]
    assert two_sum([6, 3, 5, 4], 7) == [1, 3]
    assert two_sum([4, 5, 6], 10) == [0, 2]
    assert two_sum([5, 5], 10) == [0, 1]
    assert two_sum([1, 3, 4, 2], 6) == [2, 3]

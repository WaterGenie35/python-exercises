from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Solution to LeetCode problem 347
    https://neetcode.io/problems/top-k-elements-in-list
    https://leetcode.com/problems/top-k-frequent-elements/

    Given an integer array nums and an integer k, return the k most frequent
    elements within the array.
    Assume that the k most frequent elements are unique.
    The k most frequent elements can be in any order.
    """
    num_frequency = {}
    for num in nums:
        if num in num_frequency:
            num_frequency[num] += 1
        else:
            num_frequency[num] = 1

    sorted_num_frequency = sorted(num_frequency.items(), reverse=True, key=lambda item: item[1])
    return [item[0] for item in sorted_num_frequency[:k]]


def test_solution():
    assert sorted(top_k_frequent([7, 7], 1)) == sorted([7])
    assert sorted(top_k_frequent([1, 2, 2, 3, 3, 3], 2)) == sorted([2, 3])

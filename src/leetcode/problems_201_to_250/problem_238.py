from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    """
    Solution to LeetCode problem 238
    https://neetcode.io/problems/products-of-array-discluding-self
    https://leetcode.com/problems/product-of-array-except-self/

    Given an integer array nums, return an array output where output[i] is the
    product of all the elements of nums except nums[i].
    Solve in O(n) time and without using division.
    """
    product_from_left = [1] * len(nums)
    product_from_left[0] = nums[0]
    for i in range(1, len(nums) - 1):
        product_from_left[i] = product_from_left[i - 1] * nums[i]

    product_from_right = [1] * len(nums)
    product_from_right[len(nums) - 1] = nums[-1]
    for i in range(len(nums) - 2, 0, -1):
        product_from_right[i] = product_from_right[i + 1] * nums[i]

    product = [1] * len(nums)
    for i in range(0, len(nums)):
        left = product_from_left[i - 1] if i > 0 else 1
        right = product_from_right[i + 1] if i < len(nums) - 1 else 1
        product[i] = left * right
    return product


def test_solution():
    assert product_except_self([1, 2, 4, 6]) == [48, 24, 12, 8]
    assert product_except_self([-1, 0, 1, 2, 3]) == [0, -6, 0, 0, 0]

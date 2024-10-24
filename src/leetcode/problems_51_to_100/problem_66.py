from typing import List


def plus_one(digits: List[int]) -> List[int]:
    """
    Solution to LeetCode problem 66
    https://neetcode.io/problems/plus-one
    https://leetcode.com/problems/plus-one/
    """
    result = digits.copy()
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        added_digit = digits[i] + carry
        if added_digit == 10:
            result[i] = 0
            carry = 1
        else:
            result[i] = added_digit
            carry = 0
    if carry == 1:
        result.insert(0, 1)
    return result


def test_solution():
    assert plus_one([1, 2, 3]) == [1, 2, 4]
    assert plus_one([9, 9, 9]) == [1, 0, 0, 0]

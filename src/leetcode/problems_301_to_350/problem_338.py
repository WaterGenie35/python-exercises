from typing import List


def count_bits(n: int) -> List[int]:
    """
    Solution to LeetCode problem 338
    https://neetcode.io/problems/counting-bits
    https://leetcode.com/problems/counting-bits/
    """
    num_bits = []
    for num in range(0, n + 1):
        num_bits.append(sum(int(bit) for bit in bin(num)[2:]))
    return num_bits


def test_solution():
    assert count_bits(2) == [0, 1, 1]
    assert count_bits(5) == [0, 1, 1, 2, 1, 2]

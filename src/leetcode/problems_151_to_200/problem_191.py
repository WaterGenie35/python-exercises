def hamming_weight(n: int) -> int:
    """
    Solution to LeetCode problem 191
    https://neetcode.io/problems/number-of-one-bits
    https://leetcode.com/problems/number-of-1-bits/
    """
    binary = bin(n)
    count = 0
    for bit in binary[2:]:
        count += int(bit)
    return count


def test_solution():
    assert hamming_weight(11) == 3
    assert hamming_weight(128) == 1

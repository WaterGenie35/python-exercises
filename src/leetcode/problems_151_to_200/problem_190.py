def reverse_bits(n: int) -> int:
    """
    Solution to LeetCode problem 190
    https://neetcode.io/problems/reverse-bits
    https://leetcode.com/problems/reverse-bits/
    """
    binary_n = f'{n:032b}'
    reversed_n = 0b00000000_00000000_00000000_00000000
    one_hot = 0b1
    for bit in binary_n:
        if bit == '0':
            reversed_n &= ~one_hot
        else:
            reversed_n |= one_hot
        one_hot = one_hot << 1
    return reversed_n


def test_solution():
    assert reverse_bits(21) == 2818572288

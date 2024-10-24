def is_happy(n: int) -> bool:
    """
    Solution to LeetCode problem 202
    https://neetcode.io/problems/non-cyclical-number
    https://leetcode.com/problems/happy-number/
    """
    head = n
    seen = set()
    while head not in seen:
        if head == 1:
            return True
        seen.add(head)

        sum_of_digits_squared = 0
        while head > 0:
            digit = head % 10
            sum_of_digits_squared += digit * digit
            head //= 10
        head = sum_of_digits_squared

    return False


def test_solution():
    assert is_happy(19)
    assert is_happy(100)
    assert not is_happy(2)
    assert not is_happy(101)

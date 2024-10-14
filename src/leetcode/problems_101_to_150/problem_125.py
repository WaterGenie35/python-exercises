def is_palindrome(s: str) -> bool:
    """
    Solution to LeetCode problem 125
    https://neetcode.io/problems/is-palindrome
    https://leetcode.com/problems/valid-palindrome/

    Check if the given string is a palindrome.
    Use 2 pointers.
    """
    head = 0
    tail = len(s) - 1
    while head < tail:
        head_char = s[head].lower()
        if not is_alphanumeric(head_char):
            head += 1
            continue
        tail_char = s[tail].lower()
        if not is_alphanumeric(tail_char):
            tail -= 1
            continue

        if head_char != tail_char:
            return False
        head += 1
        tail -= 1
    return True


def is_alphanumeric(char: str) -> bool:
    codepoint = ord(char)
    is_alphabetic = ord("a") <= codepoint and codepoint <= ord("z")
    is_numeric = ord("0") <= codepoint and codepoint <= ord("9")
    return is_alphabetic or is_numeric


def test_solution():
    assert is_palindrome("racecar")
    assert is_palindrome("1830110381")
    assert is_palindrome("foo 123 321 oof")
    assert is_palindrome("Was it a car or a cat I saw?")
    assert is_palindrome("-!_@#$%^&*{}[]()/.,<>?\"'+=foo bar rab oof")

    assert not is_palindrome("racecars")
    assert not is_palindrome("12345678")
    assert not is_palindrome("foo 123 321 bar")

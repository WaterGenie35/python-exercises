def is_valid(s: str) -> bool:
    """
    Solution to LeetCode problem 20
    https://neetcode.io/problems/validate-parentheses
    https://leetcode.com/problems/valid-parentheses/

    Given a string s containing just the characters (){}[], determine if the
    input string is valid.
    An input string is valid if:
      - Open brackets must be closed by the same type of brackets
      - Open brackets must be closed in the correct order
      - Every close bracket has a corresponding open bracket of the same type
    """
    stack = []
    for char in s:
        if char in ["(", "[", "{"]:
            stack.append(char)
            continue
        # char is closing bracket
        if len(stack) == 0:
            return False
        if char == ")" and stack[-1] != "(":
            return False
        if char == "]" and stack[-1] != "[":
            return False
        if char == "}" and stack[-1] != "{":
            return False
        stack.pop()
    return len(stack) == 0


def test_solution():
    assert is_valid("()")
    assert is_valid("()[]{}")
    assert is_valid("([]{{()}[]})")

    assert not is_valid("(])")

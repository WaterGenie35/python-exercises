DIGIT_FROM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
STRING_FROM = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def multiply(num1: str, num2: str) -> str:
    """
    Solution to LeetCode problem 43
    https://neetcode.io/problems/multiply-strings
    https://leetcode.com/problems/multiply-strings/

    No built-in library to convert between int and str.
    """
    int1 = 0
    for char in num1:
        digit = DIGIT_FROM[char]
        int1 *= 10
        int1 += digit

    int2 = 0
    for char in num2:
        digit = DIGIT_FROM[char]
        int2 *= 10
        int2 += digit

    product_str = ""
    remaining = int1 * int2
    if remaining == 0:
        return "0"
    while remaining > 0:
        digit = remaining % 10
        remaining //= 10
        product_str = STRING_FROM[digit] + product_str

    return product_str


def test_solution():
    assert multiply("0", "0") == "0"
    assert multiply("123", "456") == "56088"

from base64 import b64decode, b64encode
from typing import List

from utils.string import UNIT_SEPARATOR


def encode(strs: List[str]) -> str:
    """
    Solution to LeetCode problem 271
    https://neetcode.io/problems/string-encode-and-decode
    https://leetcode.com/problems/encode-and-decode-strings/

    Design an algorithm to encode a list of strings to a single string, and
    decode a single string to a list of strings.
    """
    unicode = UNIT_SEPARATOR.join(strs)
    utf8_bytes = unicode.encode('utf-8')
    b64_encoding = b64encode(utf8_bytes)
    str_repr = str(b64_encoding, 'utf-8')
    return str_repr


def decode(str: str) -> List[str]:
    utf8_bytes = b64decode(str)
    unicode = utf8_bytes.decode('utf-8')
    strs = unicode.split(UNIT_SEPARATOR)
    return strs


def test_solution():
    s1 = ["we", "say", ":", "yes"]
    assert decode(encode(s1)) == s1


# Example code to get past the neetcode env:
# class Solution:
#     def encode(self, strs: List[str]) -> str:
#         if len(strs) == 0:
#             return ""
#         unicode = chr(31) + chr(31).join(strs)
#         utf8_bytes = unicode.encode('utf-8')
#         return str(utf8_bytes, 'utf-8')

#     def decode(self, s: str) -> List[str]:
#         if s == "":
#             return []
#         return s[1:].split(chr(31))

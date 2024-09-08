from utils.string import characters_frequency


def is_anagram(s: str, t: str) -> bool:
    """
    Solution to Project Euler problem
    https://neetcode.io/problems/is-anagram
    https://leetcode.com/problems/valid-anagram/

    Check if two strings are anagrams of each other.
    Two strings are anagrams of each other if they contain the same characters
    in any order.
    """
    if len(s) != len(t):
        return False

    char_freq = characters_frequency(s)
    pair_freq = {}
    for char in t:
        if char not in char_freq:
            return False
        if char in pair_freq:
            pair_freq[char] += 1
            if pair_freq[char] > char_freq[char]:
                return False
        else:
            pair_freq[char] = 1

    return True


def test_solution():
    assert is_anagram("racecar", "carrace")

    assert not is_anagram("jar", "jam")
    assert not is_anagram("jar", "jarr")

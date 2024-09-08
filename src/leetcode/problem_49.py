from typing import List

from utils.string import characters_frequency


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Solution to LeetCode problem 49
    https://neetcode.io/problems/anagram-groups
    https://leetcode.com/problems/group-anagrams/

    Given an array of strings, group all anagrams together into sublists.
    The sublists can be in any order.
    Two strings are anagrams of each other if they contain the same characters
    in any order.
    """
    groups = []
    group_index = {}
    for str in strs:
        group = characters_frequency(str)
        group_key = tuple(sorted(group.items()))
        if group_key in group_index:
            groups[group_index[group_key]].append(str)
        else:
            group_index[group_key] = len(groups)
            groups.append([str])
    return groups


def test_solution():
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["foo"]) == [["foo"]]
    assert sorted(group_anagrams(["act", "pots", "tops", "cat", "stop", "hat"])) == sorted(
        [
            ["act", "cat"],
            ["pots", "tops", "stop"],
            ["hat"],
        ]
    )

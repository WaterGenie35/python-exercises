from typing import List


def longest_consecutive(nums: List[int]) -> int:
    """
    Solution to LeetCode problem
    https://neetcode.io/problems/longest-consecutive-sequence
    https://leetcode.com/problems/longest-consecutive-sequence/

    Given an array of integers nums, return the length of the longest
    consecutive sequence with elements in nums.
    A consecutive sequence is a sequence of elements in which each element is
    exactly 1 greater than the previous element.
    Solve in O(n) time.
    """
    longest = 0
    clusters = {}
    for num in nums:
        if num in clusters:
            # Prevents overriding cluster data that starts or ends at num.
            # Optimization is just a bonus.
            continue

        extend_start = num + 1 in clusters
        extend_end = num - 1 in clusters
        tail_length = clusters[num + 1]['length'] if extend_start else 0
        head_length = clusters[num - 1]['length'] if extend_end else 0
        cluster_length = head_length + 1 + tail_length
        if extend_start and extend_end:
            head = clusters[num - 1]
            tail = clusters[num + 1]
            start = clusters[head['start']]
            end = clusters[tail['end']]
            start['end'] = tail['end']
            end['start'] = head['start']
            start['length'] = cluster_length
            end['length'] = cluster_length
            clusters[num] = {'start': head['start'], 'end': tail['end'], 'length': cluster_length}
        elif extend_start:
            tail = clusters[num + 1]
            clusters[num] = {'start': num, 'end': tail['end'], 'length': cluster_length}
            end = clusters[tail['end']]
            end['start'] = num
            end['length'] = cluster_length
        elif extend_end:
            head = clusters[num - 1]
            clusters[num] = {'start': head['start'], 'end': num, 'length': cluster_length}
            start = clusters[head['start']]
            start['end'] = num
            start['length'] = cluster_length
        else:
            clusters[num] = {'start': num, 'end': num, 'length': cluster_length}

        longest = max(longest, cluster_length)
    return longest


def test_solution():
    assert longest_consecutive([]) == 0
    assert longest_consecutive([2, 20, 4, 10, 3, 4, 5]) == 4
    assert longest_consecutive([20, 18, 19, 1, 2, 3, 6, 5, 4, 17, 21, 16, 22]) == 7
    assert longest_consecutive([0, 3, 2, 5, 4, 6, 1, 1]) == 7
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9

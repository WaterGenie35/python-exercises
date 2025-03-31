from typing import List


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


def can_attend_meetings(intervals: List[Interval]) -> bool:
    """
    Solution to LeetCode problem 252
    https://neetcode.io/problems/meeting-schedule
    https://leetcode.com/problems/meeting-rooms/
    """
    if len(intervals) == 0:
        return True
    sorted_intervals = sorted(intervals, key=lambda interval: interval.start)
    current_interval = sorted_intervals[0]
    for next_interval in sorted_intervals[1:]:
        if next_interval.start < current_interval.end:
            return False
        current_interval = next_interval
    return True


def test_solution():
    assert can_attend_meetings([])
    assert can_attend_meetings([Interval(0, 1)])
    assert can_attend_meetings([Interval(0, 1), Interval(1, 10)])
    assert not can_attend_meetings([Interval(0, 30), Interval(5, 10)])
    assert not can_attend_meetings([Interval(0, 30), Interval(15, 40)])

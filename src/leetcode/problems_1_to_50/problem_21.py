from utils.list import ListNode
from utils.typing import Nullable


def merge_two_lists(list1: Nullable[ListNode], list2: Nullable[ListNode]) -> Nullable[ListNode]:
    """
    Solution to LeetCode problem 21
    https://neetcode.io/problems/merge-two-sorted-linked-lists
    https://leetcode.com/problems/merge-two-sorted-lists/

    Given two sorted linked lists, return a sorted list with values from both
    lists.
    """
    merged_list = None
    tail = merged_list
    head1 = list1
    head2 = list2
    while head1 is not None or head2 is not None:
        take_head1 = head2 is None or (head1 is not None and head1.val <= head2.val)
        next = ListNode(head1.val) if take_head1 else ListNode(head2.val)
        if merged_list is None:
            merged_list = tail = next
        else:
            tail.next = next
            tail = tail.next
        if take_head1:
            head1 = head1.next
        else:
            head2 = head2.next
    return merged_list


def test_solution():
    assert merge_two_lists(None, None) is None
    assert merge_two_lists(ListNode.from_list([1, 2, 4]), None) == ListNode.from_list([1, 2, 4])
    assert merge_two_lists(ListNode.from_list([1, 2, 4]), ListNode.from_list([1, 3, 5])) == ListNode.from_list(
        [1, 1, 2, 3, 4, 5]
    )
    assert merge_two_lists(ListNode.from_list([1, 2, 2, 2, 2, 2, 6]), ListNode.from_list([5])) == ListNode.from_list(
        [1, 2, 2, 2, 2, 2, 5, 6]
    )

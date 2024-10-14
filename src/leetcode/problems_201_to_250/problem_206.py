from utils.list import ListNode
from utils.typing import Nullable


def reverse_list(head: Nullable[ListNode]) -> Nullable[ListNode]:
    """
    Solution to LeetCode problem 206
    https://neetcode.io/problems/reverse-a-linked-list
    https://leetcode.com/problems/reverse-linked-list/

    Given the head of a singly linked list, return the reversed list.
    """
    current = head
    new_head = None
    while current is not None:
        new_head = ListNode(val=current.val, next=new_head)
        current = current.next
    return new_head


def test_solution():
    assert reverse_list(ListNode.from_list([])) == ListNode.from_list([])
    assert reverse_list(ListNode.from_list([1, 2, 3, 4, 5])) == ListNode.from_list([5, 4, 3, 2, 1])
    assert reverse_list(ListNode.from_list([3, 2, -5, 0, 2])) == ListNode.from_list([2, 0, -5, 2, 3])

from typing import List

from utils.typing import Nullable


class ListNode:
    def __init__(self, val: int = 0, next: Nullable['ListNode'] = None):
        self.val = val
        self.next = next

    def __eq__(self, other: 'ListNode') -> bool:
        if not isinstance(other, ListNode):
            return False
        if self.val != other.val:
            return False
        if self.next is None and other.next is not None:
            return False
        if self.next is not None and other.next is None:
            return False
        if self.next is None and other.next is None:
            return True
        return self.next == other.next

    def to_list(self) -> List[int]:
        list = []
        head = self
        while head is not None:
            list.append(head.val)
            head = head.next
        return list

    def __str__(self) -> str:
        return str(self.to_list())

    @staticmethod
    def from_list(values: List[int]) -> Nullable['ListNode']:
        head = None
        for val in reversed(values):
            head = ListNode(val, next=head)
        return head

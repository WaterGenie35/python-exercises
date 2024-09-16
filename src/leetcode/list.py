from typing import List

from utils.typing import Nullable


class ListNode:
    def __init__(self, val: int = 0, next: Nullable['ListNode'] = None):
        self.val = val
        self.next = next

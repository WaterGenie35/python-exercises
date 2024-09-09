from typing import List

from utils.typing import Nullable


def binary_search(sorted_list: List[int], target: int) -> Nullable[int]:
    if len(sorted_list) == 0:
        return None

    head = 0
    tail = len(sorted_list) - 1
    while head < tail - 1:
        mid = (head + tail) // 2
        # print(f"{head}\t{mid}\t{tail}")
        if sorted_list[mid] == target:
            return mid
        if sorted_list[mid] < target:
            head = mid
        else:
            tail = mid

    if sorted_list[head] == target:
        return head
    if sorted_list[tail] == target:
        return tail
    return None

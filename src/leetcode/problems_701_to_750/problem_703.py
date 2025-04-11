from typing import List


class KthLargest:
    """
    Solution to LeetCode problem 703
    https://neetcode.io/problems/kth-largest-integer-in-a-stream
    https://leetcode.com/problems/kth-largest-element-in-a-stream/

    Define a class that can accept integers and returns the kth largest integers
    accepted so far.
    The constructor will be initialized with at least k integers.
    """

    # We implement min-heap of size k.
    # The kth largest is the root of this min-heap.
    def __init__(self, k: int, nums: List[int]):
        assert len(nums) >= k

        self.size = k
        self.min_heap_array = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap_array) == 0:
            self.min_heap_array.append(val)
            return val
        self.min_heap_array.append(val)
        self.__bubble_up(len(self.min_heap_array) - 1)
        if len(self.min_heap_array) > self.size:
            # Trimming is insufficient because right subtree can be less than
            # left subtree
            remaining_k = self.min_heap_array[1:]
            self.min_heap_array = []
            for num in remaining_k:
                self.add(num)
        return self.min_heap_array[0]

    def __bubble_up(self, node_index: int):
        if node_index == 0:
            return
        parent_index = (node_index - 1) // 2
        node_value = self.min_heap_array[node_index]
        parent_value = self.min_heap_array[parent_index]
        if node_value < parent_value:
            self.min_heap_array[parent_index] = node_value
            self.min_heap_array[node_index] = parent_value
            self.__bubble_up(parent_index)


def test_solution():
    test_1 = KthLargest(5, [3, 10, 7, 11, 12])
    assert test_1.add(5) == 5

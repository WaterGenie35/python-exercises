from queue import Queue
from typing import List

from utils.tree import TreeNode
from utils.typing import Nullable


def right_side_view(root: Nullable[TreeNode]) -> List[int]:
    """
    Solution to LeetCode problem 199
    https://neetcode.io/problems/binary-tree-right-side-view
    https://leetcode.com/problems/binary-tree-right-side-view/

    Given a tree, return a list of node values that are visible from the right.
    A node is visible from the right if it is the right-most node on its level.
    """
    # Level-order
    traversal_queue = Queue()
    traversal_queue.put({'node': root, 'level': 0})
    last_level = 0
    last_value = None
    view = []
    while traversal_queue.qsize() > 0:
        item = traversal_queue.get()
        node = item['node']
        level = item['level']
        if node is None:
            continue
        traversal_queue.put({'node': node.left, 'level': level + 1})
        traversal_queue.put({'node': node.right, 'level': level + 1})

        if last_level < level:
            view.append(last_value)
        last_value = node.val
        last_level = level

    # last iteration
    if last_value is not None:
        view.append(last_value)

    return view


def test_solution():
    assert right_side_view(TreeNode.from_list([1, 2, 3, 4, 5, 6, 7])) == [1, 3, 7]
    assert right_side_view(TreeNode.from_list([1, 2, 3, 4])) == [1, 3, 4]
    assert right_side_view(TreeNode.from_list([1, 2, 3, 4, 5])) == [1, 3, 5]
    assert right_side_view(TreeNode.from_list([1, 2, 3, None, 5])) == [1, 3, 5]

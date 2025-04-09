from queue import Queue
from typing import List

from utils.tree import TreeNode
from utils.typing import Nullable


def level_order(root: Nullable[TreeNode]) -> List[List[int]]:
    """
    Solution to LeetCode problem 102
    https://neetcode.io/problems/level-order-traversal-of-binary-tree
    https://leetcode.com/problems/binary-tree-level-order-traversal/

    Given a binary tree, return the list of lists of nodes in each level in level order.
    """
    traversal_queue = Queue()
    traversal_queue.put({'node': root, 'level': 0})
    traversal_list = []
    while traversal_queue.qsize() > 0:
        item = traversal_queue.get()
        node = item['node']
        level = item['level']
        if node is None:
            continue
        if len(traversal_list) < level + 1:
            traversal_list.append([])
        traversal_list[-1].append(node.val)
        traversal_queue.put({'node': node.left, 'level': level + 1})
        traversal_queue.put({'node': node.right, 'level': level + 1})
    return traversal_list


def test_solution():
    assert level_order(None) == []
    assert level_order(TreeNode(1)) == [[1]]
    assert level_order(TreeNode.from_list([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]

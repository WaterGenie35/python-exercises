from utils.tree import TreeNode
from utils.typing import Nullable


def is_same_tree(root1: Nullable[TreeNode], root2: Nullable[TreeNode]) -> bool:
    """
    Solution to LeetCode problem 100
    https://neetcode.io/problems/same-binary-tree
    https://leetcode.com/problems/same-tree/

    Check if the 2 given binary trees are equal.
    """
    stack1 = [root1]
    stack2 = [root2]
    while len(stack1) > 0:
        item1 = stack1.pop()
        item2 = stack2.pop()
        if item1 is None and item2 is None:
            continue
        if item1 is None or item2 is None:
            return False
        if item1.val != item2.val:
            return False
        stack1.append(item1.left)
        stack1.append(item1.right)
        stack2.append(item2.left)
        stack2.append(item2.right)

    return len(stack2) == 0


def test_solution():
    assert is_same_tree(None, None)
    assert is_same_tree(TreeNode(1), TreeNode(1))
    assert not is_same_tree(TreeNode(1), TreeNode(2))
    assert is_same_tree(TreeNode.from_list([1, 2, 3, None, 4, 5, 6]), TreeNode.from_list([1, 2, 3, None, 4, 5, 6]))
    assert not is_same_tree(TreeNode.from_list([1, 2, 3, None, 4, 5, 6]), TreeNode.from_list([1, 2, 3, 4, None, 5, 6]))

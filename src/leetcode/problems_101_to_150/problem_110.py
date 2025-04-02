from typing import Tuple

from utils.tree import TreeNode
from utils.typing import Nullable


def is_balanced(root: Nullable[TreeNode]) -> bool:
    """
    Solution to LeetCode problem 110
    https://neetcode.io/problems/balanced-binary-tree
    https://leetcode.com/problems/balanced-binary-tree/

    Check if the given binary tree is height-balanced.
    A binary tree is height-balanced if the depth of the two subtrees of every
    node differ by 0 or 1.
    """
    return is_balanced_recurse(root)[0]


def is_balanced_recurse(node: Nullable[TreeNode]) -> Tuple[bool, int]:
    if node is None:
        return (True, 0)
    if node.left is None and node.right is None:
        return (True, 1)
    left = (True, 0) if node.left is None else is_balanced_recurse(node.left)
    right = (True, 0) if node.right is None else is_balanced_recurse(node.right)
    height = max(left[1], right[1]) + 1
    balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
    return (balanced, height)


def test_solution():
    assert is_balanced(None)
    assert is_balanced(TreeNode(1))
    assert not is_balanced(TreeNode(1, TreeNode(2, TreeNode(3))))
    assert not is_balanced(TreeNode(1, TreeNode(2), TreeNode(2, TreeNode(3), TreeNode(3, TreeNode(4), TreeNode(4)))))
    assert is_balanced(
        TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(2, TreeNode(3), TreeNode(3, TreeNode(4), TreeNode(4))))
    )

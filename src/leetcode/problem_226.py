from utils.tree import TreeNode
from utils.typing import Nullable


def invert_tree(root: Nullable[TreeNode]) -> Nullable[TreeNode]:
    """
    Solution to LeetCode problem 226
    https://neetcode.io/problems/invert-a-binary-tree
    https://leetcode.com/problems/invert-binary-tree/

    Invert the given binary tree.
    """
    # Using stack as an exercise
    if root is None:
        return None

    inverted = TreeNode(root.val)
    original_stack = [root]
    inverted_stack = [inverted]
    while len(original_stack) > 0:
        original_head = original_stack.pop()
        inverted_head = inverted_stack.pop()

        inverted_head.left = TreeNode(original_head.right.val) if original_head.right is not None else None
        inverted_head.right = TreeNode(original_head.left.val) if original_head.left is not None else None

        if original_head.left is not None:
            original_stack.append(original_head.left)
            inverted_stack.append(inverted_head.right)
        if original_head.right is not None:
            original_stack.append(original_head.right)
            inverted_stack.append(inverted_head.left)
    return inverted


def test_solution():
    assert invert_tree(None) is None

    tree_1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    inverted_1 = TreeNode(4, TreeNode(7, TreeNode(9), TreeNode(6)), TreeNode(2, TreeNode(3), TreeNode(1)))
    assert invert_tree(tree_1) == inverted_1

    tree_2 = TreeNode(4, None, TreeNode(7, TreeNode(6), None))
    inverted_2 = TreeNode(4, TreeNode(7, None, TreeNode(6)), None)
    assert invert_tree(tree_2) == inverted_2

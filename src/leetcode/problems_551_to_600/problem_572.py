from utils.tree import TreeNode
from utils.typing import Nullable


def is_subtree(root: Nullable[TreeNode], subtree: Nullable[TreeNode]) -> bool:
    """
    Solution to LeetCode problem 572
    https://neetcode.io/problems/subtree-of-a-binary-tree
    https://leetcode.com/problems/subtree-of-another-tree/

    Check if the given tree is a subtree of another tree.
    """
    if subtree is None:
        return True
    traversal_stack = [root]
    while len(traversal_stack) > 0:
        node = traversal_stack.pop()
        if node is None:
            continue
        traversal_stack.append(node.left)
        traversal_stack.append(node.right)
        if is_same_tree(node, subtree):
            return True
    return False


def is_same_tree(tree1: Nullable[TreeNode], tree2: Nullable[TreeNode]) -> bool:
    tree1_stack = [tree1]
    tree2_stack = [tree2]
    while len(tree1_stack) > 0:
        if len(tree2_stack) == 0:
            return False

        self_head = tree1_stack.pop()
        other_head = tree2_stack.pop()
        if self_head is None and other_head is None:
            continue
        if self_head is None or other_head is None or self_head.val != other_head.val:
            return False

        tree1_stack.append(self_head.left)
        tree2_stack.append(other_head.left)

        tree1_stack.append(self_head.right)
        tree2_stack.append(other_head.right)

    return len(tree1_stack) == len(tree2_stack)


def test_solution():
    assert is_subtree(TreeNode.from_list([3, 4, 5, 1, 2]), TreeNode.from_list([4, 1, 2]))
    assert not is_subtree(TreeNode.from_list([3, 4, 5, 1, 2, None, None, None, None, 0]), TreeNode.from_list([4, 1, 2]))

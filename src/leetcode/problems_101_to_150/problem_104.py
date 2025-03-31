from utils.tree import TreeNode
from utils.typing import Nullable


def max_depth(root: Nullable[TreeNode]) -> int:
    """
    Solution to LeetCode problem 104
    https://neetcode.io/problems/depth-of-binary-tree
    https://leetcode.com/problems/maximum-depth-of-binary-tree/

    Find the maximum depth of the given binary tree.
    """
    max_depth = 0
    stack = [{'node': root, 'depth': 0}]
    while len(stack) > 0:
        item = stack.pop()
        node = item['node']
        depth = item['depth']
        if node is None:
            continue

        stack.append({'node': node.left, 'depth': depth + 1})
        stack.append({'node': node.right, 'depth': depth + 1})
        max_depth = max(max_depth, depth + 1)

    return max_depth


def test_solution():
    assert max_depth(None) == 0

    tree_1 = TreeNode(1, None, TreeNode(2))
    assert max_depth(tree_1) == 2

    tree_2 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(tree_2) == 3

from typing import Tuple

from utils.tree import TreeNode
from utils.typing import Nullable


def diameter(root: Nullable[TreeNode]) -> int:
    """
    Solution to LeetCode problem 543
    https://neetcode.io/problems/binary-tree-diameter
    https://leetcode.com/problems/diameter-of-binary-tree/

    Find the diameter of the given binary tree.
    The diameter is the length of the longest path between any two nodes.
    The length of a path between two nodes is the number of edges between them.
    """
    return max(diameter_recurse(root))


def diameter_recurse(node: Nullable[TreeNode]) -> Tuple[int, int]:
    if node is None or (node.left is None and node.right is None):
        return (0, 0)
    left = (0, 0) if node.left is None else diameter_recurse(node.left)
    right = (0, 0) if node.right is None else diameter_recurse(node.right)
    longest_path_to_node = max(left[0], right[0]) + 1
    path_through_node = 0
    if node.left is not None and node.right is not None:
        path_through_node = left[0] + right[0] + 2
    longest_path_overall = max(path_through_node, left[1], right[1])
    return (longest_path_to_node, longest_path_overall)


def test_solution():
    assert diameter(TreeNode(1)) == 0
    assert diameter(TreeNode(1, TreeNode(2))) == 1
    assert diameter(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))) == 3
    assert (
        diameter(
            TreeNode(
                4,
                TreeNode(-7),
                TreeNode(
                    -3,
                    TreeNode(
                        -9,
                        TreeNode(9, TreeNode(6, TreeNode(0, TreeNode(-1)), TreeNode(6, TreeNode(-4)))),
                        TreeNode(-7, TreeNode(-6, TreeNode(5)), TreeNode(-6, TreeNode(9, TreeNode(-2)))),
                    ),
                    TreeNode(-3, TreeNode(-4)),
                ),
            )
        )
        == 8
    )

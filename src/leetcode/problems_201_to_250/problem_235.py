from utils.tree import TreeNode


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Solution to LeetCode problem 235
    https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree
    https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

    Given a binary search tree and 2 noes from the tree,
    find the lowest common ancestor of the 2 nodes.
    The ancestor can be the node itself.
    """
    p_val = p.val
    q_val = q.val
    if p_val > q_val:
        tmp = p_val
        p_val = q_val
        q_val = tmp

    traversal_stack = [root]
    while len(traversal_stack) > 0:
        node = traversal_stack.pop()
        if node is None:
            continue

        if node.val == p_val or node.val == q_val:
            return node

        if p_val < node.val and node.val < q_val:
            return node

        if node.val > q_val:
            traversal_stack.append(node.left)
        else:
            traversal_stack.append(node.right)

    return root


def test_solution():
    p = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5)))
    q = TreeNode(8, TreeNode(7), TreeNode(9))
    root = TreeNode(6, p, q)
    assert lowest_common_ancestor(root, p, q).val == 6

    q = TreeNode(4, TreeNode(3), TreeNode(5))
    p = TreeNode(2, TreeNode(0), q)
    root = TreeNode(6, p, TreeNode(8, TreeNode(7), TreeNode(9)))
    assert lowest_common_ancestor(root, p, q).val == 2

    q = TreeNode(1)
    p = TreeNode(2, q)
    assert lowest_common_ancestor(root, p, q).val == 2

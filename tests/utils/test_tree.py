from utils.tree import TreeNode, in_order_traversal, post_order_traversal, pre_order_traversal

TEST_TREE = TreeNode(
    6,
    TreeNode(2, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(5))),
    TreeNode(7, None, TreeNode(9, TreeNode(8), None)),
)


def test_pre_order_traversal():
    expected_order = [6, 2, 1, 4, 3, 5, 7, 9, 8]
    actual_order = list(pre_order_traversal(TEST_TREE))
    for i in range(len(actual_order)):
        assert expected_order[i] == actual_order[i].val


def test_post_order_traversal():
    expected_order = [1, 3, 5, 4, 2, 8, 9, 7, 6]
    actual_order = list(post_order_traversal(TEST_TREE))
    for i in range(len(actual_order)):
        assert expected_order[i] == actual_order[i].val


def test_in_order_traversal():
    expected_order = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    actual_order = list(in_order_traversal(TEST_TREE))
    for i in range(len(actual_order)):
        assert expected_order[i] == actual_order[i].val


def test_from_list():
    list1 = []
    assert TreeNode.from_list(list1) is None
    list2 = [5]
    assert TreeNode.from_list(list2) == TreeNode(5)
    list3 = [5, 5, 2, 4, None, 6, 8, None, None, None, None, None, None, 14]
    assert TreeNode.from_list(list3) == TreeNode(
        5, TreeNode(5, TreeNode(4)), TreeNode(2, TreeNode(6), TreeNode(8, TreeNode(14)))
    )

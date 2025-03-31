from collections.abc import Iterator

from utils.typing import Nullable


class TreeNode:
    def __init__(self, val: int = 0, left: Nullable['TreeNode'] = None, right: Nullable['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other: 'TreeNode') -> bool:
        self_stack = [self]
        other_stack = [other]
        while len(self_stack) > 0:
            if len(other_stack) == 0:
                return False

            self_head = self_stack.pop()
            other_head = other_stack.pop()
            if self_head is None and other_head is None:
                continue
            if self_head is None or other_head is None or self_head.val != other_head.val:
                return False

            self_stack.append(self_head.left)
            other_stack.append(other_head.left)

            self_stack.append(self_head.right)
            other_stack.append(other_head.right)

        return len(self_stack) == len(other_stack)


def pre_order_traversal(root: Nullable[TreeNode]) -> Iterator[TreeNode]:
    # stack = [root]
    # while len(stack) > 0:
    #     node = stack.pop()
    #     if node is None:
    #         continue

    #     yield node
    #     stack.append(node.right)
    #     stack.append(node.left)
    if root is None:
        return
    yield root
    yield from pre_order_traversal(root.left)
    yield from pre_order_traversal(root.right)


def post_order_traversal(root: Nullable[TreeNode]) -> Iterator[TreeNode]:
    if root is None:
        return
    yield from post_order_traversal(root.left)
    yield from post_order_traversal(root.right)
    yield root


def in_order_traversal(root: Nullable[TreeNode]) -> Iterator[TreeNode]:
    if root is None:
        return
    yield from in_order_traversal(root.left)
    yield root
    yield from in_order_traversal(root.right)

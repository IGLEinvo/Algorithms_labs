import unittest


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branch_sums(root):
    def helper(node, is_left):
        if not node:
            return 0

        if not node.left and not node.right and is_left:
            return node.value

        return helper(node.left, True) + helper(node.right, False)

    return helper(root, False)


class TestBinaryTree(unittest.TestCase):
    def test_branch_sums(self):
        root = BinaryTree(3)
        root.left = BinaryTree(5)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(7)
        root.right.right = BinaryTree(7)

        self.assertEqual(branch_sums(root), 12)

    def test_branch_sums_with_only_root(self):
        root = BinaryTree(3)
        self.assertEqual(branch_sums(root), 0)

    def test_empty_tree(self):
        root = None
        self.assertEqual(branch_sums(root), 0)

    def test_unbalanced_tree(self):
        root = BinaryTree(3)
        root.left = BinaryTree(5)
        root.left.left = BinaryTree(10)
        root.left.left.left = BinaryTree(20)
        self.assertEqual(branch_sums(root), 20)

    def test_large_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)
        root.left.left.left = BinaryTree(8)
        self.assertEqual(branch_sums(root), 14)

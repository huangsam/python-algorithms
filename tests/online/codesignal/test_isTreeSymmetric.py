import algorithms.online.codesignal.isTreeSymmetric as symmetry
from algorithms.collection.tree import TreeNode


class TestIsTreeSymmetric:
    def test_symmetric(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right = TreeNode(2)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        assert symmetry.isTreeSymmetric(root)

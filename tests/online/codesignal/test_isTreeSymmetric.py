from algorithms.collection.tree import TreeNode
from algorithms.online.codesignal import isTreeSymmetric as symmetry


class TestIsTreeSymmetric:
    def test_symmetric_good(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right = TreeNode(2)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        assert symmetry.isTreeSymmetric(root)

    def test_symmetric_bad(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        assert not symmetry.isTreeSymmetric(root)

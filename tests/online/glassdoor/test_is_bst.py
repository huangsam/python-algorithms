from collection.tree import TreeNode
from online.glassdoor.is_bst import is_bst


class TestIsBST(object):

    def test_is_bst_good(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(5)
        assert is_bst(root) is True

    def test_is_bst_bad_general(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(5)
        flag = is_bst(root)
        assert flag is False

    def test_is_bst_bad_left(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.left.right = TreeNode(5)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(7)
        assert is_bst(root) is False

    def test_is_bst_bad_right(self):
        root = TreeNode(2)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.left.left = TreeNode(1)
        assert is_bst(root) is False

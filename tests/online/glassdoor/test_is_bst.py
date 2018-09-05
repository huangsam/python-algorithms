from collection.tree import TreeNode
from online.glassdoor.is_bst import is_bst


class TestIsBST(object):

    def test_is_bst_good(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(5)
        val, flag = is_bst(root)
        assert val == root.val and flag is True

    def test_is_bst_bad(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(5)
        val, flag = is_bst(root)
        assert val is None and flag is False

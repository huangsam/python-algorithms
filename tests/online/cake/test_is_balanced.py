from collection.tree import TreeNode
from online.cake.is_balanced import is_balanced


class TestIsBalanced(object):

    def test_is_balanced(self):
        root = TreeNode(6)
        root.insert_left(3)
        root.insert_right(4)
        root.left.insert_left(2)
        root.left.insert_right(7)
        root.right.insert_left(10)
        root.right.insert_right(8)
        root.right.right.insert_right(9)
        assert is_balanced(root) is True

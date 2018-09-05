from graph.creation import (
    create_postorder_inorder,
    create_preorder_inorder,
)
from graph.inorder import inorder_recursive


class TestCreation(object):

    def test_create_postorder_inorder(self):
        postorder = [6,7,5,3,4,2,1]
        postrange = (0, len(postorder)-1)
        inorder = [6,5,7,1,3,2,4]
        inrange = (0, len(inorder)-1)
        root = create_postorder_inorder(postorder, postrange, inorder, inrange)
        assert root.val == 1
        assert root.left.val == 5
        assert root.right.val == 2
        assert inorder_recursive(root) == inorder

    def test_create_postorder_inorder(self):
        preorder = [1,5,6,7,2,3,4]
        prerange = (0, len(preorder)-1)
        inorder = [6,5,7,1,3,2,4]
        inrange = (0, len(inorder)-1)
        root = create_preorder_inorder(preorder, prerange, inorder, inrange)
        assert root.val == 1
        assert root.left.val == 5
        assert root.right.val == 2
        assert inorder_recursive(root) == inorder

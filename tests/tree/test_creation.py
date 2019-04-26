import pytest

from algorithms.tree import creation as create
from algorithms.tree import inorder as ins


@pytest.mark.tree
class TestCreation:
    def test_create_postorder_inorder(self):
        postorder = [6, 7, 5, 3, 4, 2, 1]
        postrange = (0, len(postorder) - 1)
        inorder = [6, 5, 7, 1, 3, 2, 4]
        inrange = (0, len(inorder) - 1)
        root = create.create_postorder_inorder(postorder, postrange, inorder, inrange)
        assert root is not None and root.val == 1
        assert ins.inorder_recursive(root) == inorder

    def test_create_preorder_inorder(self):
        preorder = [1, 5, 6, 7, 2, 3, 4]
        prerange = (0, len(preorder) - 1)
        inorder = [6, 5, 7, 1, 3, 2, 4]
        inrange = (0, len(inorder) - 1)
        root = create.create_preorder_inorder(preorder, prerange, inorder, inrange)
        assert root is not None and root.val == 1
        assert ins.inorder_recursive(root) == inorder
from collection.tree import TreeNode
from graph.postorder import postorder_recursive


class TestPostorder(object):

    def test_postorder_recursive(self, simple_tree):
        result = postorder_recursive(simple_tree)
        assert(len(result)) == 6
        assert '3,5,6,4,2,1' == ','.join(map(str, result))

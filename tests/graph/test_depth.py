from collection.graph import Graph
from graph.depth import dfs


class TestDFS(object):

    def test_dfs(self):
        graph = Graph(
            ('a', 'b'),
            ('a', 'c'),
            ('b', 'd'),
            ('c', 'e')
        )
        order = dfs(graph, 'a')
        assert len(order) == len(graph.get_nodes())
        assert 'acebd' == ''.join(order)

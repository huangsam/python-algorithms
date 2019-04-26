import pytest

from algorithms.graph.breadth import bfs


@pytest.mark.graph
class TestBFS:
    def test_bfs(self, simple_graph):
        order = bfs(simple_graph, "a")
        assert len(order) == len(simple_graph.get_nodes())
        assert "a,b,c,d,e" == ",".join(order)

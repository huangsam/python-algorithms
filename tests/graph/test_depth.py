import pytest

from graph.depth import dfs


@pytest.mark.graph
class TestDFS:
    def test_dfs(self, simple_graph):
        order = dfs(simple_graph, "a")
        assert len(order) == len(simple_graph.get_nodes())
        assert "a,c,e,b,d" == ",".join(order)

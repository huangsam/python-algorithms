import pytest

from algorithms.graph.depth import dfs


@pytest.mark.graph
def test_dfs(simple_graph):
    order = dfs(simple_graph, "a")
    assert len(order) == len(simple_graph.get_nodes())
    assert "a,c,e,b,d" == ",".join(order)

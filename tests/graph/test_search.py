import pytest

from algorithms.graph.search import bfs, dfs


@pytest.mark.graph
def test_bfs(simple_graph):
    order = bfs(simple_graph, "a")
    assert len(order) == len(simple_graph.get_nodes())
    assert "a,b,c,d,e" == ",".join(order)


@pytest.mark.graph
def test_dfs(simple_graph):
    order = dfs(simple_graph, "a")
    assert len(order) == len(simple_graph.get_nodes())
    assert "a,c,e,b,d" == ",".join(order)

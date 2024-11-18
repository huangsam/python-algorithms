import pytest

from algorithms.graph.search import bfs, dfs


@pytest.mark.graph
def test_bfs(acyclic_digraph):
    order = bfs(acyclic_digraph, "a")
    assert len(order) == len(acyclic_digraph.get_nodes())
    assert "a,b,c,d,e" == ",".join(order)


@pytest.mark.graph
def test_dfs(acyclic_digraph):
    order = dfs(acyclic_digraph, "a")
    assert len(order) == len(acyclic_digraph.get_nodes())
    assert "a,c,e,b,d" == ",".join(order)

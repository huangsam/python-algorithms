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


@pytest.mark.graph
def test_bfs_cyclic(cyclic_digraph):
    order = bfs(cyclic_digraph, "a")
    assert len(order) == len(cyclic_digraph.get_nodes())
    assert set(order) == {"a", "b", "c", "d"}


@pytest.mark.graph
def test_dfs_cyclic(cyclic_digraph):
    order = dfs(cyclic_digraph, "a")
    assert len(order) == len(cyclic_digraph.get_nodes())
    assert set(order) == {"a", "b", "c", "d"}

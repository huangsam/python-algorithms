import pytest

from algorithms.collection.graph import DirectedGraph, UndirectedGraph

_SAMPLE_DATA = (("a", "b"), ("a", "c"), ("a", "d"))


@pytest.mark.graph
def test_setup_directed():
    graph = DirectedGraph(*_SAMPLE_DATA)
    assert len(graph.get_nodes()) == 4


@pytest.mark.graph
def test_add_edge_directed():
    graph = DirectedGraph()
    for src, dst in _SAMPLE_DATA:
        graph.add_edge(src, dst)
    assert len(graph.get_nodes()) == 4


@pytest.mark.graph
def test_get_children_directed():
    graph = DirectedGraph(*_SAMPLE_DATA)
    children = graph.get_children("a")
    assert len(children) == len(_SAMPLE_DATA)
    assert "b" in children
    assert "c" in children


@pytest.mark.graph
def test_get_out_degree_directed():
    graph = DirectedGraph(*_SAMPLE_DATA)
    assert graph.get_out_degree("a") == 3
    assert graph.get_out_degree("d") == 0


@pytest.mark.graph
def test_get_in_degree_directed():
    graph = DirectedGraph(*_SAMPLE_DATA)
    assert graph.get_in_degree("a") == 0
    for child in graph.get_children("a"):
        assert graph.get_in_degree(child) == 1


@pytest.mark.graph
def test_check_node_directed():
    graph = DirectedGraph(*_SAMPLE_DATA)
    for node in graph.get_nodes():
        assert graph.check_node(node)


@pytest.mark.graph
def test_check_edge_directed():
    graph = DirectedGraph(*_SAMPLE_DATA)
    assert graph.check_edge(("a", "b"))
    assert not graph.check_edge(("b", "a"))


@pytest.mark.graph
def test_setup_undirected():
    graph = UndirectedGraph(*_SAMPLE_DATA)
    assert len(graph.get_nodes()) == 4


@pytest.mark.graph
def test_get_out_degree_undirected():
    graph = UndirectedGraph(*_SAMPLE_DATA)
    assert graph.get_out_degree("a") == 3
    assert graph.get_out_degree("d") == 1


@pytest.mark.graph
def test_get_in_degree_undirected():
    graph = UndirectedGraph(*_SAMPLE_DATA)
    assert graph.get_in_degree("a") == 3
    for child in graph.get_children("a"):
        assert graph.get_in_degree(child) == 1


@pytest.mark.graph
def test_check_node_undirected():
    graph = UndirectedGraph(*_SAMPLE_DATA)
    for node in graph.get_nodes():
        assert graph.check_node(node)


@pytest.mark.graph
def test_check_edge_undirected():
    graph = UndirectedGraph(*_SAMPLE_DATA)
    assert graph.check_edge(("a", "b"))
    assert graph.check_edge(("b", "a"))

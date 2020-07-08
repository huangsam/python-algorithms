import pytest

from algorithms.collection.graph import DirectedGraph, UndirectedGraph

SAMPLE_DATA = (("a", "b"), ("a", "c"), ("a", "d"))


@pytest.mark.graph
class TestDirectedGraph:
    def test_setup_directed(self):
        graph = DirectedGraph(*SAMPLE_DATA)
        assert len(graph.get_nodes()) == 4

    def test_add_edge_directed(self):
        graph = DirectedGraph()
        for src, dst in SAMPLE_DATA:
            graph.add_edge(src, dst)
        assert len(graph.get_nodes()) == 4

    def test_get_children_directed(self):
        graph = DirectedGraph(*SAMPLE_DATA)
        children = graph.get_children("a")
        assert len(children) == len(SAMPLE_DATA)
        assert "b" in children
        assert "c" in children

    def test_get_out_degree_directed(self):
        graph = DirectedGraph(*SAMPLE_DATA)
        assert graph.get_out_degree("a") == 3
        assert graph.get_out_degree("d") == 0

    def test_get_in_degree_directed(self):
        graph = DirectedGraph(*SAMPLE_DATA)
        assert graph.get_in_degree("a") == 0
        for child in graph.get_children("a"):
            assert graph.get_in_degree(child) == 1

    def test_check_node_directed(self):
        graph = DirectedGraph(*SAMPLE_DATA)
        for node in graph.get_nodes():
            assert graph.check_node(node)

    def test_check_edge_directed(self):
        graph = DirectedGraph(*SAMPLE_DATA)
        assert graph.check_edge(("a", "b"))
        assert not graph.check_edge(("b", "a"))


@pytest.mark.graph
class TestUndirectedGraph:
    def test_setup_undirected(self):
        graph = UndirectedGraph(*SAMPLE_DATA)
        assert len(graph.get_nodes()) == 4

    def test_get_out_degree_undirected(self):
        graph = UndirectedGraph(*SAMPLE_DATA)
        assert graph.get_out_degree("a") == 3
        assert graph.get_out_degree("d") == 1

    def test_get_in_degree_undirected(self):
        graph = UndirectedGraph(*SAMPLE_DATA)
        assert graph.get_in_degree("a") == 3
        for child in graph.get_children("a"):
            assert graph.get_in_degree(child) == 1

    def test_check_node_undirected(self):
        graph = UndirectedGraph(*SAMPLE_DATA)
        for node in graph.get_nodes():
            assert graph.check_node(node)

    def test_check_edge_undirected(self):
        graph = UndirectedGraph(*SAMPLE_DATA)
        assert graph.check_edge(("a", "b"))
        assert graph.check_edge(("b", "a"))

import pytest

from algorithms.collection.graph import Graph


@pytest.mark.graph
class TestGraph:

    SAMPLE_DATA = (("a", "b"), ("a", "c"), ("a", "d"))

    def test_setup(self):
        graph = Graph(*self.SAMPLE_DATA)
        assert len(graph.get_nodes()) == 4

    def test_add_edge(self):
        graph = Graph()
        for src, dst in self.SAMPLE_DATA:
            graph.add_edge(src, dst)
        assert len(graph.get_nodes()) == 4

    def test_get_children(self):
        graph = Graph(*self.SAMPLE_DATA)
        children = graph.get_children("a")
        assert len(children) == len(self.SAMPLE_DATA)
        assert "b" in children
        assert "c" in children

    def test_get_out_degree(self):
        graph = Graph(*self.SAMPLE_DATA)
        assert graph.get_out_degree("a") == 3
        assert graph.get_out_degree("d") == 0

    def test_get_in_degree(self):
        graph = Graph(*self.SAMPLE_DATA)
        assert graph.get_in_degree("a") == 0
        for child in graph.get_children("a"):
            assert graph.get_in_degree(child) == 1

    def test_check_node(self):
        graph = Graph(*self.SAMPLE_DATA)
        for node in graph.get_nodes():
            assert graph.check_node(node)

    def test_check_edge(self):
        graph = Graph(*self.SAMPLE_DATA)
        assert graph.check_edge(("a", "b"))
        assert not graph.check_edge(("b", "a"))

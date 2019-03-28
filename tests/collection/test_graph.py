import pytest

from collection.graph import Graph


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

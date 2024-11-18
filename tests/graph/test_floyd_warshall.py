import pytest

from algorithms.constants import MAX_INT
from algorithms.graph.floyd_warshall import floyd_warshall, transitive_closure


@pytest.mark.graph
@pytest.mark.dynamic
def test_floyd_warshall():
    graph = [
        [0, 5, MAX_INT, 10],
        [MAX_INT, 0, 3, MAX_INT],
        [MAX_INT, MAX_INT, 0, 1],
        [MAX_INT, MAX_INT, MAX_INT, 0],
    ]
    result = floyd_warshall(graph)
    assert result == [
        [0, 5, 8, 9],
        [MAX_INT, 0, 3, 4],
        [MAX_INT, MAX_INT, 0, 1],
        [MAX_INT, MAX_INT, MAX_INT, 0],
    ]


@pytest.mark.graph
@pytest.mark.dynamic
def test_transitive_closure():
    graph = [[1, 1, 1, 1], [0, 1, 1, 0], [1, 0, 1, 1], [0, 0, 0, 1]]
    result = transitive_closure(graph)
    assert result == [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 1]]

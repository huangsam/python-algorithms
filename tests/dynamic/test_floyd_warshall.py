import pytest

from algorithms.constants import MAX_INT
import algorithms.dynamic.floyd_warshall as floyd


@pytest.mark.graph
@pytest.mark.dynamic
class TestFloydWarshall:
    def test_floyd_warshall(self):
        graph = [
            [0, 5, MAX_INT, 10],
            [MAX_INT, 0, 3, MAX_INT],
            [MAX_INT, MAX_INT, 0, 1],
            [MAX_INT, MAX_INT, MAX_INT, 0],
        ]
        result = floyd.floyd_warshall(graph)
        assert isinstance(result, list)
        assert isinstance(result[0], list)
        assert graph[0][3] == 10
        assert result[0][3] == 9

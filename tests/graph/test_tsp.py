import pytest

from algorithms.graph.tsp import tsp_brute


@pytest.mark.graph
def test_tsp_brute_1():
    graph = [[0]]
    result = tsp_brute(graph, 0)
    assert result == 0


@pytest.mark.graph
def test_tsp_brute_2():
    graph = [[0, 20], [10, 0]]
    result = tsp_brute(graph, 0)
    assert result == 30


@pytest.mark.graph
def test_tsp_brute_4():
    graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    result = tsp_brute(graph, 0)
    assert result == 80

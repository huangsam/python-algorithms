from algorithms.dynamic import tsp


class TestTsp:
    def test_tsp_brute_1(self):
        graph = [[0]]
        result = tsp.tsp_brute(graph, 0)
        assert result == 0

    def test_tsp_brute_2(self):
        graph = [[0, 20], [10, 0]]
        result = tsp.tsp_brute(graph, 0)
        assert result == 30

    def test_tsp_brute_4(self):
        graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
        result = tsp.tsp_brute(graph, 0)
        assert result == 80

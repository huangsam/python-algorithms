from algorithms.online.dailycoding.max_weight_path import max_weight_path


class TestMaxWeightPath:
    def test_max_weight_path(self):
        triangle = [[1], [2, 3], [1, 5, 1]]
        assert max_weight_path(triangle) == 1 + 3 + 5

    def test_max_weight_corner(self):
        triangle = [[1], [10, 1], [1, 1, 100]]
        assert max_weight_path(triangle) == 1 + 1 + 100

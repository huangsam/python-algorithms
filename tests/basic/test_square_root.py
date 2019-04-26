import pytest

from algorithms.basic.square_root import square_root


class TestSquareRoot:
    @pytest.mark.parametrize("root, x", [(3.0, 9), (6.0, 36), (9.0, 81), (12.0, 144)])
    def test_square_root_exact(self, root, x):
        assert root == square_root(x)

    @pytest.mark.parametrize(
        "left, right, x",
        [
            (2.0, 3.0, 7),
            (4.0, 5.0, 18),
            (5.0, 6.0, 30),
            (11.0, 12.0, 130),
            (14.0, 15.0, 200),
        ],
    )
    def test_square_root_about(self, left, right, x):
        assert left < square_root(x) < right

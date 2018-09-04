import pytest

from basic.square_root import square_root


class TestSquareRoot(object):

    @pytest.parametrize("root, x", [
        (9.0, 81),
        (12.0, 144),
        (13.0, 169),
    ])
    def test_square_root_exact(self, root, x):
        assert root == square_root(x)

    @pytest.parametrize("left, right, x", [
        (14.0, 15.0, 200),
        (12.0, 13.0, 130),
        (2.0, 3.0, 7),
    ])
    def test_square_root_about(self, left, right, x):
        assert left < square_root(x) < right

import pytest

from algorithms.dynamic import max_square as maxsq


@pytest.mark.array
@pytest.mark.dynamic
class TestMaxSquare:
    @pytest.mark.parametrize("i", [1, 2, 3, 4])
    def test_max_square_empty(self, i):
        m = [[0] * i for _ in range(i)]
        assert maxsq.max_square(m) == 0

    @pytest.mark.parametrize("i", [1, 2, 3, 4])
    def test_max_square_full(self, i):
        m = [[1] * i for _ in range(i)]
        assert maxsq.max_square(m) == i

    def test_max_square_partial(self):
        m = [[0, 0, 0], [1, 1, 1], [1, 1, 1]]
        assert maxsq.max_square(m) == 2

    def test_max_square_one(self):
        m = [[0, 0, 0], [0, 0, 0], [1, 1, 1]]
        assert maxsq.max_square(m) == 1

import pytest

from algorithms.dynamic.lis import lis


@pytest.mark.array
@pytest.mark.dynamic
class TestLis:
    @pytest.mark.parametrize("n", [1, 5, 100])
    def test_lis_always(self, n):
        a = [_ for _ in range(n)]
        assert lis(a) == n

    @pytest.mark.parametrize("n", [1, 5, 100])
    def test_lis_never(self, n):
        a = [_ for _ in range(n - 1, -1, -1)]
        assert lis(a) == 1

    def test_lis_mixed_small(self):
        a = [1, 12, 7]
        assert lis(a) == 2

    def test_lis_mixed_big(self):
        a = [1, 12, 7, 0, 23, 11, 52, 31, 61, 69, 70, 2]
        assert lis(a) == 7

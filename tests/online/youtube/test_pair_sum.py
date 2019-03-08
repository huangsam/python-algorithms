import pytest

from online.youtube.pair_sum import pair_sum


@pytest.fixture(scope="function")
def array():
    return [3, 7, 10, 9, 1, 5]


@pytest.mark.array
class TestPairSum(object):
    def test_pair_sum_multiple(self, array):
        target = 10
        result = pair_sum(array, target)
        assert len(result) == 2
        assert (5, 5) not in result
        assert (7, 3) in result
        assert (1, 9) in result

    def test_pair_sum_single(self, array):
        target = 15
        result = pair_sum(array, target)
        assert len(result) == 1
        assert (5, 10) in result

    def test_pair_sum_none(self, array):
        target = 2
        result = pair_sum(array, target)
        assert len(result) == 0

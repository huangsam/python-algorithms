import pytest

from online.geeks.powerset import powerset


class TestPowerSet(object):
    @pytest.mark.parametrize("size", [0, 1, 2, 3, 5, 8])
    def test_powerset(self, size):
        vals = tuple([val for val in range(size)])
        result = list(powerset(vals))
        assert len(result) == 2 ** size

import pytest

from algorithms.math.powerset import powerset


@pytest.mark.math
@pytest.mark.parametrize("size", [0, 1, 2, 3, 5, 8])
def test_powerset(size):
    vals = tuple([val for val in range(size)])
    result = list(powerset(vals))
    assert len(result) == 2 ** size

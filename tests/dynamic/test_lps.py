import pytest

from algorithms.dynamic.lps import lps_dp


@pytest.mark.string
@pytest.mark.dynamic
@pytest.mark.parametrize("i, o", [("geeksforgeeks", 5)])
def test_lps_all(i: str, o: int):
    assert lps_dp(i) == o

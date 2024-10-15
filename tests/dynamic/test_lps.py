import pytest

from algorithms.dynamic import lps


@pytest.mark.string
@pytest.mark.dynamic
@pytest.mark.parametrize("i, o", [("geeksforgeeks", 5)])
def test_lps_all(i: str, o: int):
    assert lps.lps_dp(i) == o

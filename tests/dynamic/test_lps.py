import pytest

from algorithms.dynamic import lps


@pytest.mark.string
@pytest.mark.dynamic
class TestLps:
    @pytest.mark.parametrize("i, o", [("geeksforgeeks", 5)])
    def test_lps_all(self, i, o):
        assert lps.lps_dp(i) == o

import pytest

from algorithms.dynamic import lcs


@pytest.mark.string
@pytest.mark.dynamic
class TestLcs:
    def test_lcs_all(self):
        astr = "abcd"
        bstr = "abcd"
        assert lcs.lcs_rec(astr, bstr) == 4

    def test_lcs_partial(self):
        astr = "abcd"
        bstr = "abcadf"
        assert lcs.lcs_rec(astr, bstr) == 4

    def test_lcs_none(self):
        astr = "abcd"
        bstr = "efgh"
        assert lcs.lcs_rec(astr, bstr) == 0

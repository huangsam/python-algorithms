import pytest

from algorithms.dynamic import lcs


@pytest.mark.string
@pytest.mark.dynamic
class TestLcs:
    @pytest.mark.parametrize(
        "a, b, o",
        [
            ("a", "a", 1),
            ("abcd", "abcd", 4),
            ("abcd", "abcdef", 4),
            ("fadeway", "aw", 2),
        ],
    )
    def test_lcs_all(self, a, b, o):
        assert lcs.lcs_rec(a, b) == o

    @pytest.mark.parametrize(
        "a, b, o",
        [
            ("ai", "abcdefghi", 2),
            ("ali", "abcdefghi", 2),
            ("aeghijklmnop", "abcdefghi", 5),
        ],
    )
    def test_lcs_partial(self, a, b, o):
        assert lcs.lcs_rec(a, b) == o

    def test_lcs_none(self):
        astr = "abcd"
        bstr = "efgh"
        assert lcs.lcs_rec(astr, bstr) == 0

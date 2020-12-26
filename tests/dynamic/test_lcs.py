import pytest

from algorithms.dynamic import lcs


@pytest.mark.string
@pytest.mark.dynamic
@pytest.mark.parametrize(
    "a, b, o",
    [
        ("a", "a", 1),
        ("abcd", "abcd", 4),
        ("abcd", "abcdef", 4),
        ("fadeway", "aw", 2),
    ],
)
@pytest.mark.parametrize("f", [lcs.lcs_rec, lcs.lcs_dp])
def test_lcs_all(f, a, b, o):
    assert f(a, b) == o


@pytest.mark.string
@pytest.mark.dynamic
@pytest.mark.parametrize(
    "a, b, o",
    [
        ("ai", "abcdefghi", 2),
        ("ali", "abcdefghi", 2),
        ("allli", "abcdefghi", 2),
        ("aeghij", "abcdefghi", 5),
    ],
)
@pytest.mark.parametrize("f", [lcs.lcs_rec, lcs.lcs_dp])
def test_lcs_partial(f, a, b, o):
    assert lcs.lcs_rec(a, b) == o


@pytest.mark.string
@pytest.mark.dynamic
@pytest.mark.parametrize("a, b", [("", ""), ("a", "b"), ("abcd", "efgh")])
@pytest.mark.parametrize("f", [lcs.lcs_rec, lcs.lcs_dp])
def test_lcs_none(f, a, b):
    assert f(a, b) == 0

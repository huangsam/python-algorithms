import pytest

from algorithms.dynamic.lcs import lcs_dp, lcs_rec


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
@pytest.mark.parametrize("f", [lcs_rec, lcs_dp])
def test_lcs_all(f, a: str, b: str, o: int):
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
@pytest.mark.parametrize("f", [lcs_rec, lcs_dp])
def test_lcs_partial(f, a: str, b: str, o: int):
    assert f(a, b) == o


@pytest.mark.string
@pytest.mark.dynamic
@pytest.mark.parametrize("a, b", [("", ""), ("a", "b"), ("abcd", "efgh")])
@pytest.mark.parametrize("f", [lcs_rec, lcs_dp])
def test_lcs_none(f, a: str, b: str):
    assert f(a, b) == 0

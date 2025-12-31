import pytest

from algorithms.string import word_search


@pytest.mark.string
@pytest.mark.parametrize(
    "astr, bstr, ix",
    [
        ("hello", "", -1),
        ("ab", "abc", -1),
        ("hello", "helli", -1),
        ("hello", "hello", 0),
        ("hello world i am trying", "i am", 12),
        ("hello world", "world", 6),
    ],
)
def test_naive(astr, bstr, ix):
    assert word_search.naive(astr, bstr) == ix


@pytest.mark.string
def test_naive_not_found():
    assert word_search.naive("hello", "xyz") == -1

import pytest

from algorithms.basic import word_search as wsearch


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
    assert wsearch.naive(astr, bstr) == ix

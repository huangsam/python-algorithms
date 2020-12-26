import pytest

from algorithms.dynamic import split_palin as palin


@pytest.mark.string
@pytest.mark.dynamic
@pytest.mark.parametrize(
    "i, o",
    [
        ("", 0),
        ("aba", 0),
        ("abaa", 1),
        ("ababbbbb", 1),
        ("xabaay", 3),
        ("abcde", 4),
    ],
)
def test_split_palin(i, o):
    result = palin.split_palin(i, cache={})
    assert result == o

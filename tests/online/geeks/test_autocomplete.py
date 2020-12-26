import pytest

from algorithms.online.geeks.autocomplete import autocomplete


@pytest.mark.string
@pytest.mark.tree
@pytest.mark.parametrize(
    "s, queries, expected",
    [
        ("de", ["dog", "deer", "deal"], ["deer", "deal"]),
        ("ab", ["abc", "abcd", "aa", "abbbaba"], ["abc", "abcd", "abbbaba"]),
        ("c", ["cat", "catch", "catcher"], ["cat", "catch", "catcher"]),
        ("b", ["ham", "clam"], []),
        ("", ["a", "ab"], ["a", "ab"]),
    ],
)
def test_autocomplete(s, queries, expected):
    result = autocomplete(s, queries)
    assert set(result) == set(expected)

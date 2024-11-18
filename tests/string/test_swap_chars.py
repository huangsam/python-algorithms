import pytest

from algorithms.string.swap_chars import swap_chars, swap_chars_optimal


@pytest.mark.string
@pytest.mark.parametrize(
    "a, b, o",
    [
        ("", "", True),
        ("a", "ab", False),
        ("a", "a", True),
        ("aa", "aa", True),
        ("aaaa", "aaaa", True),
        ("abcd", "abcd", True),
        ("abc", "cba", True),
        ("cdab", "abcd", True),
        ("a", "b", False),
        ("ab", "ba", False),
        ("cdab", "dcba", False),
    ],
)
@pytest.mark.parametrize("f", [swap_chars, swap_chars_optimal])
def test_swap_chars_bad_length(f, a, b, o):
    assert f(a, b) is o

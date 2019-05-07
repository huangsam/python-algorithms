import pytest

import algorithms.online.geeks.swap_chars as swap


@pytest.mark.string
class TestSwapChars:
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
            ("ab", "ba", False),
            ("cdab", "dcba", False),
        ],
    )
    def test_swap_chars_bad_length(self, a, b, o):
        assert swap.swap_chars(a, b) is o

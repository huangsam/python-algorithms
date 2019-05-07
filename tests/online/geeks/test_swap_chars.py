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
            ("a", "b", False),
            ("ab", "ba", False),
            ("cdab", "dcba", False),
        ],
    )
    @pytest.mark.parametrize("f", [swap.swap_chars, swap.swap_chars_optimal])
    def test_swap_chars_bad_length(self, f, a, b, o):
        assert f(a, b) is o

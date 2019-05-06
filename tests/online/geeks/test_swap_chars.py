import pytest

import algorithms.online.geeks.swap_chars as swap


@pytest.mark.string
class TestSwapChars:
    def test_swap_chars_bad_length(self):
        assert swap.swap_chars("a", "ab") is False

    def test_swap_chars_same(self):
        assert swap.swap_chars("abcd", "abcd") is True

    def test_swap_chars_diff_can(self):
        assert swap.swap_chars("cdab", "abcd") is True

    def test_swap_chars_diff_cannot(self):
        assert swap.swap_chars("cdab", "dcba") is False

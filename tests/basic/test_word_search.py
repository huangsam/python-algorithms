import pytest

import algorithms.basic.word_search as wsearch


@pytest.mark.string
class TestNaive:
    def test_naive(self):
        assert wsearch.naive("hello", "") == -1
        assert wsearch.naive("hello", "hello") == 0
        assert wsearch.naive("hello", "helli") == -1
        assert wsearch.naive("hello world i am trying", "i am") != -1

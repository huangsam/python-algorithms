import pytest

from algorithms.online.word_wrap import word_wrap


@pytest.mark.online
def test_word_wrap():
    words = ["hello", "world"]
    result = word_wrap(words, 10)
    assert isinstance(result, str)
    assert result == "hello_____\nworld_____"

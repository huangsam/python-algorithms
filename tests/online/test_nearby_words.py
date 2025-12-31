import pytest

from algorithms.online.nearby_words import get_nearby_chars, is_word, nearby_permutations, nearby_words


@pytest.mark.online
def test_get_nearby_chars():
    assert get_nearby_chars("c") == {"c", "b", "h", "k", "t", "r"}
    assert get_nearby_chars("a") == {"a", "e", "o", "i", "u"}
    assert get_nearby_chars("x") == set()


@pytest.mark.online
def test_is_word():
    assert is_word("cat") is True
    assert is_word("dog") is False


@pytest.mark.online
def test_nearby_permutations():
    result = nearby_permutations("a", 0)
    assert "a" in result
    assert "e" in result
    assert "o" in result
    assert "i" in result
    assert "u" in result


@pytest.mark.online
def test_nearby_words():
    result = nearby_words("cat")
    assert "cat" in result
    assert "hat" in result
    assert "bat" in result

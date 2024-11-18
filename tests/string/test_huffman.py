import pytest

from algorithms.string.huffman import huffman


@pytest.mark.string
@pytest.mark.tree
def test_huffman():
    frequencies = {"a": 15, "b": 7, "c": 6, "d": 6, "e": 5}
    result = huffman(frequencies)
    assert result == {"a": "0", "e": "100", "c": "101", "d": "110", "b": "111"}

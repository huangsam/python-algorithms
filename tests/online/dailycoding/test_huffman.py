import pytest

from algorithms.online.dailycoding import huffman as huff


@pytest.mark.string
@pytest.mark.tree
def test_huffman():
    frequencies = {"a": 15, "b": 7, "c": 6, "d": 6, "e": 5}
    result = huff.huffman(frequencies)
    assert result == {"a": "0", "e": "100", "c": "101", "d": "110", "b": "111"}

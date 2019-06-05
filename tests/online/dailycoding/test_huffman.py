import pytest

import algorithms.online.dailycoding.huffman as huff


@pytest.mark.string
@pytest.mark.tree
class TestHuffman:
    def test_huffman(self):
        frequencies = {"a": 15, "b": 7, "c": 6, "d": 6, "e": 5}
        result = huff.huffman(frequencies)
        assert result == {"a": "0", "e": "100", "c": "101", "d": "110", "b": "111"}

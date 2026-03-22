import pytest

from algorithms.collections.bloom_filter import BloomFilter


@pytest.mark.collections
def test_bloom_filter_add_contains():
    bf = BloomFilter(100, 5)
    bf.add("test")
    assert "test" in bf


@pytest.mark.collections
def test_bloom_filter_not_contains():
    bf = BloomFilter(1000, 5)
    bf.add("apple")
    # Small chance of false positive, but with 1000 slots and 1 item it's extremely low
    assert "banana" not in bf


@pytest.mark.collections
def test_bloom_filter_false_positive():
    # Force false positive with very small size
    bf = BloomFilter(1, 1)
    bf.add("a")
    assert "b" in bf  # Collides in 1-slot filter

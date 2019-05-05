import pytest

from algorithms.sorting import merge_in_place as mip
from tests.utils import is_sorted


@pytest.mark.array
@pytest.mark.sorting
class TestMergeInPlace:
    def test_merge_in_place_a(self):
        a = [1, 2]
        b = []
        mip.merge_in_place(a, b)
        assert is_sorted(a)

    def test_merge_in_place_b(self):
        a = [None, None]
        b = [1, 2]
        mip.merge_in_place(a, b)
        assert is_sorted(a)

    def test_merge_in_place_unique(self):
        a = [1, 2, 3, None, None, None]
        b = [4, 5, 6]
        mip.merge_in_place(a, b)
        assert is_sorted(a)

    def test_merge_in_place_zigzag(self):
        a = [1, 3, 5, None, None, None]
        b = [2, 4, 6]
        mip.merge_in_place(a, b)
        assert is_sorted(a)

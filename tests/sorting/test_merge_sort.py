import pytest

from algorithms.sorting import merge_sort
from tests.utils import is_sorted


@pytest.mark.array
@pytest.mark.sorting
class TestMergeSort:
    def test_merge_sort(self, array):
        assert not is_sorted(array)
        merge_sort.sort(array)
        assert is_sorted(array)

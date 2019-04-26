import pytest

from algorithms.basic.merge_simple import merge_sort


@pytest.mark.array
@pytest.mark.sorting
class TestMergeSimpleSort:
    @staticmethod
    def _is_sorted(array):
        alen = len(array)
        for i in range(1, alen):
            if array[i - 1] > array[i]:
                return False
        return True

    def test_merge_simple(self, array):
        assert not self._is_sorted(array)
        array = merge_sort(array)
        assert self._is_sorted(array)

    def test_merge_empty(self):
        arr = []
        actual = merge_sort(arr)
        assert actual == arr

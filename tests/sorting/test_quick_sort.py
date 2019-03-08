import pytest

from sorting import quick_sort


@pytest.mark.array
@pytest.mark.sorting
class TestQuickSort(object):
    @staticmethod
    def _is_sorted(array):
        alen = len(array)
        for i in range(1, alen):
            if array[i - 1] > array[i]:
                return False
        return True

    def test_quick_sort_iterative(self, array):
        assert not self._is_sorted(array)
        quick_sort.sort(array)
        assert self._is_sorted(array)

    def test_quick_sort_recursive(self, array):
        assert not self._is_sorted(array)
        quick_sort.sort(array, iterative=False)
        assert self._is_sorted(array)

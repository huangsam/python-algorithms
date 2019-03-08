import pytest

from sorting import selection_sort


@pytest.mark.array
@pytest.mark.sorting
class TestSelectionSort(object):
    @staticmethod
    def _is_sorted(array):
        alen = len(array)
        for i in range(1, alen):
            if array[i - 1] > array[i]:
                return False
        return True

    def test_selection_sort(self, array):
        assert not self._is_sorted(array)
        selection_sort.sort(array)
        assert self._is_sorted(array)

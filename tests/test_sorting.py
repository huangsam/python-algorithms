from sorting import (
    bubble_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    selection_sort,
)


class TestSorting(object):

    @staticmethod
    def _is_sorted(array):
        alen = len(array)
        for i in range(1, alen):
            if array[i-1] > array[i]:
                return False
        return True

    def test_bubble_sort(self, array):
        assert not self._is_sorted(array)
        bubble_sort.sort(array)
        assert self._is_sorted(array)

    def test_insertion_sort(self, array):
        assert not self._is_sorted(array)
        insertion_sort.sort(array)
        assert self._is_sorted(array)

    def test_merge_sort(self, array):
        assert not self._is_sorted(array)
        merge_sort.sort(array)
        assert self._is_sorted(array)

    def test_quick_sort_iterative(self, array):
        assert not self._is_sorted(array)
        quick_sort.sort(array)
        assert self._is_sorted(array)

    def test_quick_sort_recursive(self, array):
        assert not self._is_sorted(array)
        quick_sort.sort(array, iterative=False)
        assert self._is_sorted(array)

    def test_selection_sort(self, array):
        assert not self._is_sorted(array)
        selection_sort.sort(array)
        assert self._is_sorted(array)

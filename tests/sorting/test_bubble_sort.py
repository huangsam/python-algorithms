from sorting import bubble_sort


class TestSort(object):

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

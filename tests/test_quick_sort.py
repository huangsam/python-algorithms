from random import randint

from sorting import quick_sort


class TestSort():

    def test_quick_sort(self, array):
        quick_sort.sort(array)
        alen = len(array)
        for i in range(1, alen):
            assert array[i-1] <= array[i]

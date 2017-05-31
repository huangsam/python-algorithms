from sorting import quick_sort


class TestSort():

    def test_quick_sort_iterative(self, array):
        quick_sort.sort(array)
        alen = len(array)
        for i in range(1, alen):
            assert array[i-1] <= array[i]

    def test_quick_sort_recursive(self, array):
        quick_sort.sort(array, iterative=False)
        alen = len(array)
        for i in range(1, alen):
            assert array[i-1] <= array[i]

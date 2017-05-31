from sorting import selection_sort


class TestSort():

    def test_selection_sort(self, array):
        selection_sort.sort(array)
        alen = len(array)
        for i in range(1, alen):
            assert array[i-1] <= array[i]

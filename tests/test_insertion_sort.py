from sorting import insertion_sort


class TestSort():

    def test_insertion_sort(self, array):
        insertion_sort.sort(array)
        alen = len(array)
        for i in range(1, alen):
            assert array[i-1] <= array[i]

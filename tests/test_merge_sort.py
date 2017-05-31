from sorting import merge_sort


class TestSort():

    def test_merge_sort(self, array):
        merge_sort.sort(array)
        alen = len(array)
        for i in range(1, alen):
            assert array[i-1] <= array[i]

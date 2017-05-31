from sorting import bubble_sort


class TestSort():

    def test_bubble_sort(self, array):
        bubble_sort.sort(array)
        alen = len(array)
        for i in range(1, alen):
            assert array[i-1] <= array[i]

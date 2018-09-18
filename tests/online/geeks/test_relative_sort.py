from online.geeks.relative_sort import relative_sort


class TestRelativeSort(object):

    def test_relative_sort_a1(self):
        a1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
        a2 = [2, 1, 8, 3]
        expected = [2, 2, 1, 1, 8, 8, 3, 5, 6, 7, 9]
        for i, j in zip(relative_sort(a1, a2), expected):
            assert i == j

    def test_relative_sort_a2(self):
        a1 = [2, 1, 8, 3]
        a2 = [1, 8]
        expected = [1, 8, 2, 3]
        for i, j in zip(relative_sort(a1, a2), expected):
            assert i == j

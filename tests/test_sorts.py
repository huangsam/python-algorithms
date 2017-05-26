from random import randint

from sorting import bubble_sort
from sorting import insertion_sort
from sorting import merge_sort
from sorting import quick_sort


class TestSort():

    sample_size = int(10**4/2)

    def setup_method(self, test_method):
        self.A = [randint(0, 100) for i in range(self.sample_size)]
        self.expected = list(sorted(self.A))

    def test_bubble_sort(self):
        assert self.A != self.expected
        bubble_sort.sort(self.A)
        assert self.A == self.expected

    def test_insertion_sort(self):
        assert self.A != self.expected
        insertion_sort.sort(self.A)
        assert self.A == self.expected

    def test_merge_sort(self):
        assert self.A != self.expected
        merge_sort.sort(self.A)
        assert self.A == self.expected

    def test_quick_sort(self):
        assert self.A != self.expected
        quick_sort.sort(self.A)
        assert self.A == self.expected

    def teardown_method(self, test_method):
        self.A, self.expected = [], []

from random import randint

from sorting import selection_sort


class TestSort():

    sample_size = int(10**3)

    def setup_method(self, test_method):
        self.A = [randint(0, 100) for i in range(self.sample_size)]
        self.expected = list(sorted(self.A))

    def test_selection_sort(self):
        assert self.A != self.expected
        selection_sort.sort(self.A)
        assert self.A == self.expected

    def teardown_method(self, test_method):
        self.A, self.expected = [], []

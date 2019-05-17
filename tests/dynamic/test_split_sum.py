import algorithms.dynamic.split_sum as split


class TestSplitSum:
    def test_split_sum_one(self):
        assert split.split_sum([1, 2, 3, 4], 1) == 10

    def test_split_sum_two(self):
        assert split.split_sum([1, 2, 3, 4], 2) == 6

    def test_split_sum_three(self):
        assert split.split_sum([1, 2, 3, 4], 3) == 4

    def test_split_sum_all(self):
        assert split.split_sum([1, 2, 3, 4], 4) == 4

    def test_split_sum_sample(self):
        assert split.split_sum([5, 1, 2, 7, 3, 4], 3) == 8

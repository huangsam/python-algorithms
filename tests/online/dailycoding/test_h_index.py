import algorithms.online.dailycoding.h_index as hind


class TestHIndex:
    def test_h_index_sample(self):
        assert hind.h_index([4, 3, 0, 1, 5]) == 3

    def test_h_index_zero(self):
        assert hind.h_index([0, 0, 0, 0, 0]) == 0

    def test_h_index_one(self):
        assert hind.h_index([1, 1, 1, 1, 1]) == 1

    def test_h_index_same(self):
        for i in range(1, 10):
            papers = [i for _ in range(i)]
            assert hind.h_index(papers) == i

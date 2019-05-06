import pytest

import algorithms.online.geeks.dutch_flag as dutch


@pytest.mark.array
class TestDutchFlag:
    @staticmethod
    def verify(arr):
        i = 0
        for j in (0, 1, 2):
            while i < len(arr) and arr[i] == j:
                i += 1
        assert i == len(arr)

    def test_dutch_flag_sample(self):
        arr = [0, 1, 2, 0, 1, 2]
        result = dutch.dutch_flag(arr)
        self.verify(result)

    def test_dutch_flag_done(self):
        arr = [0, 0, 1, 1, 2, 2]
        result = dutch.dutch_flag(arr)
        self.verify(result)

    @pytest.mark.parametrize("n", [0, 1, 2])
    def test_dutch_flag_all_n(self, n):
        arr = [n for i in range(6)]
        result = dutch.dutch_flag(arr)
        self.verify(result)

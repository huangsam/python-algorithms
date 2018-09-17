import pytest

from online.glassdoor.merge_k import merge_k


class TestMergeK(object):

    @pytest.mark.parametrize('arrays, expected', [
        (
            [[10, 15, 30], [12, 15, 20], [17, 20, 32]],
            [10, 12, 15, 15, 17, 20, 20, 30, 32],
        ),
        (
            [],
            [],
        ),
        (
            [[], [], []],
            [],
        ),
        (
            [[], [1], [1, 2]],
            [1, 1, 2],
        ),
        (
            [[1]],
            [1],
        ),
        (
            [[1], [1, 3, 5], [1, 10, 20, 30, 40]],
            [1, 1, 1, 3, 5, 10, 20, 30, 40],
        ),
    ])
    def test_merge_k(self, arrays, expected):
        result = merge_k(arrays)
        for i, j in zip(result, expected):
            assert i == j

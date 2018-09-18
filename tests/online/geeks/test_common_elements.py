import pytest

from online.geeks.common_elements import common_elements


class TestCommonElements(object):

    @pytest.mark.parametrize('a1, a2, a3, expected', [
        ([1, 3, 5, 7, 9], [1, 5, 9], [3, 5, 7, 9], [5, 9]),
        ([1, 1, 1, 3], [1, 3], [1, 1], [1]),
    ])
    def test_common_elements(self, a1, a2, a3, expected):
        result = common_elements(a1, a2, a3)
        for i, j in zip(result, expected):
            assert i == j

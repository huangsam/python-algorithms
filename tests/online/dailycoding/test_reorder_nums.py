import pytest

import algorithms.online.dailycoding.reorder_nums as reorder


@pytest.mark.array
@pytest.mark.sorting
class TestReorderNums:
    def test_reorder_nums(self):
        result = reorder.reorder_nums([None, "+", "+", "-", "+"])
        assert len(result) > 0
        assert result == [1, 2, 3, 0, 4]

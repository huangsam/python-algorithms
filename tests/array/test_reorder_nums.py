import pytest

from algorithms.array import reorder_nums as reorder


@pytest.mark.array
@pytest.mark.sorting
def test_reorder_nums():
    result = reorder.reorder_nums([None, "+", "+", "-", "+"])
    assert len(result) > 0
    assert result == [1, 2, 3, 0, 4]

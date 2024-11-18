import pytest

from algorithms.array.reorder_nums import reorder_nums


@pytest.mark.array
@pytest.mark.sorting
def test_reorder_nums():
    result = reorder_nums([None, "+", "+", "-", "+"])
    assert len(result) > 0
    assert result == [1, 2, 3, 0, 4]

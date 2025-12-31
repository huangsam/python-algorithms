import pytest

from algorithms.online.zig_zag import zig_zag


@pytest.mark.online
def test_zig_zag():
    result = zig_zag("abc", 2)
    assert len(result) == 2
    assert len(result[0]) == 3
    assert result == [["a", " ", "c"], [" ", "b", " "]]

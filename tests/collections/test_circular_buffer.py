import pytest

from algorithms.collections.circular_buffer import CircularBuffer


@pytest.mark.collections
def test_circular_buffer_append():
    cb = CircularBuffer(3)
    cb.append(1)
    cb.append(2)
    cb.append(3)
    assert cb.to_list() == [1, 2, 3]


@pytest.mark.collections
def test_circular_buffer_overwrite():
    cb = CircularBuffer(3)
    cb.append(1)
    cb.append(2)
    cb.append(3)
    cb.append(4)
    assert cb.to_list() == [2, 3, 4]


@pytest.mark.collections
def test_circular_buffer_get():
    cb = CircularBuffer(3)
    cb.append(1)
    cb.append(2)
    assert cb.get() == 1
    assert cb.to_list() == [2]


@pytest.mark.collections
def test_circular_buffer_empty_get():
    cb = CircularBuffer(3)
    with pytest.raises(IndexError):
        cb.get()


@pytest.mark.collections
def test_circular_buffer_len():
    cb = CircularBuffer(3)
    cb.append(1)
    cb.append(2)
    assert len(cb) == 2


@pytest.mark.collections
def test_circular_buffer_getitem():
    cb = CircularBuffer(3)
    cb.append(1)
    cb.append(2)
    cb.append(3)
    cb.append(4)
    assert cb[0] == 2
    assert cb[1] == 3
    assert cb[2] == 4

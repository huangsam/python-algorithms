import pytest

from algorithms.array.stack_machine import stack_machine


@pytest.mark.string
@pytest.mark.stack
@pytest.mark.parametrize("i, o", [("13+62*7+*", 76), ("11+", 2)])
def test_stack_machine_good(i: str, o: int):
    assert stack_machine(i) == o


@pytest.mark.string
@pytest.mark.stack
def test_stack_machine_pop_by_one():
    assert stack_machine("11++") == -1


@pytest.mark.string
@pytest.mark.stack
def test_stack_machine_overflow():
    assert stack_machine("2" * 100 + "*" * 99) == -1

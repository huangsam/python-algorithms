import pytest

from algorithms.array import stack_machine as sm


@pytest.mark.string
@pytest.mark.stack
@pytest.mark.parametrize("i, o", [("13+62*7+*", 76), ("11+", 2)])
def test_stack_machine_good(i, o):
    assert sm.stack_machine(i) == o


@pytest.mark.string
@pytest.mark.stack
def test_stack_machine_pop_by_one():
    assert sm.stack_machine("11++") == -1


@pytest.mark.string
@pytest.mark.stack
def test_stack_machine_overflow():
    assert sm.stack_machine("2" * 32 + "*" * 31) == -1

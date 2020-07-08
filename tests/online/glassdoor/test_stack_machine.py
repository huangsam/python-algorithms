import pytest

from algorithms.online.glassdoor import stack_machine as sm


@pytest.mark.string
@pytest.mark.stack
class TestStackMachine:
    @pytest.mark.parametrize("i, o", [("13+62*7+*", 76), ("11+", 2)])
    def test_stack_machine_good(self, i, o):
        assert sm.stack_machine(i) == o

    def test_stack_machine_pop_by_one(self):
        assert sm.stack_machine("11++") == -1

    def test_stack_machine_overflow(self):
        assert sm.stack_machine("2" * 32 + "*" * 31) == -1

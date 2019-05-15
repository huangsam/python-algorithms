import pytest

import algorithms.online.geeks.stack_machine as sm


@pytest.mark.string
@pytest.mark.stack
class TestStackMachine:
    @pytest.mark.parametrize("i, o", [("13+62*7+*", 76), ("11+", 2), ("11++", -1)])
    def test_stack_machine(self, i, o):
        assert sm.stack_machine(i) == o

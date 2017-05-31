from random import randint

import pytest


SAMPLE_SIZE = int(10**3)


@pytest.fixture(scope="session",
                autouse=True,
                params=[10, 100, 1000])
def array(request):
    return [randint(0, 100) for i in range(request.param)]

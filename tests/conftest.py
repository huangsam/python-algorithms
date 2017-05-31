from random import randint

import pytest


@pytest.fixture(scope="session",
                autouse=True,
                params=[50, 100, 400])
def array(request):
    return [randint(0, 100) for i in range(request.param)]

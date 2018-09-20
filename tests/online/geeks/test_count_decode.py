import pytest

from online.geeks.count_decode import count_decode


class TestCountDecode(object):

    @pytest.mark.parametrize('digits, expected', [
        ('111', 3),
        ('1234', 3),
        ('11', 2),
        ('1', 1),
        ('', 1),
    ])
    def test_count_decode(self, digits, expected):
        assert count_decode(digits) == expected

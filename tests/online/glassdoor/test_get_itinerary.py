import pytest

from online.glassdoor.get_itinerary import get_itinerary


class TestGetItinerary(object):

    @pytest.mark.parametrize('start, flights, expected', [
        (
            'YUL',
            [('HNL', 'AKL'), ('YUL', 'ORD'), ('ORD', 'SFO'), ('SFO', 'HNL')],
            ['YUL', 'ORD', 'SFO', 'HNL', 'AKL'],
        ),
        (
            'YUL',
            [('SFO', 'HNL'), ('YUL', 'ORD')],
            None,
        ),
        (
            'SFO',
            [('SFO', 'HNL'), ('SFO', 'ORD')],
            None,
        ),
        (
            'SFO',
            [('SFO', 'HNL'), ('HNL', 'SFO')],
            ['SFO', 'HNL', 'SFO'],
        ),
        (
            'HNL',
            [('SFO', 'HNL'), ('HNL', 'SFO')],
            ['HNL', 'SFO', 'HNL'],
        ),
    ])
    def test_get_itinerary(self, start, flights, expected):
        result = get_itinerary(start, flights)
        if result is None:
            assert result == expected
        else:
            for i, j in zip(result, expected):
                assert i == j

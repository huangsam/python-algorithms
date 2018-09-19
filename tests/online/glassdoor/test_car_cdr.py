from online.glassdoor.car_cdr import (
    car, cdr, cons
)


class TestCarCdr(object):

    def test_car(self):
        assert car(cons(3, 4)) == 3

    def test_cdr(self):
        assert cdr(cons(3, 4)) == 4

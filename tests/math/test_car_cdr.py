from algorithms.math.car_cdr import car, cdr, cons


def test_car():
    assert car(cons(3, 4)) == 3


def test_cdr():
    assert cdr(cons(3, 4)) == 4

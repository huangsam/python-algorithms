from algorithms.math import car_cdr as lisp


def test_car():
    assert lisp.car(lisp.cons(3, 4)) == 3


def test_cdr():
    assert lisp.cdr(lisp.cons(3, 4)) == 4

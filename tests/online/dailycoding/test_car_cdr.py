from algorithms.online.dailycoding import car_cdr as lisp


class TestCarCdr:
    def test_car(self):
        assert lisp.car(lisp.cons(3, 4)) == 3

    def test_cdr(self):
        assert lisp.cdr(lisp.cons(3, 4)) == 4

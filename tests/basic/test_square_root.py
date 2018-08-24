from basic.square_root import square_root


class TestSquareRoot(object):

    def test_square_root_exact(self):
        assert 9.0 == square_root(81)
        assert 12.0 == square_root(144)
        assert 13.0 == square_root(169)

    def test_square_root_about(self):
        assert 14.0 < square_root(200) and square_root(200) < 15.0

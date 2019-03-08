from online.cake.rectangular_love import Rectangle, rectangular_love


class TestRectangularLove(object):
    def test_rectangular_love_good(self):
        rect1 = Rectangle((4, 8), (8, 4))
        rect2 = Rectangle((2, 10), (10, 2))
        assert rectangular_love(rect1, rect2) is True

    def test_rectangular_love_bad(self):
        rect1 = Rectangle((4, 8), (8, 4))
        rect2 = Rectangle((0, 2), (2, 0))
        assert rectangular_love(rect1, rect2) is False

    def test_rectangular_love_corner(self):
        rect1 = Rectangle((4, 8), (8, 4))
        rect2 = Rectangle((0, 4), (4, 0))
        assert rectangular_love(rect1, rect2) is True

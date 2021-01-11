class Rectangle:
    def __init__(self, top_left, bottom_right):
        self.left, self.top = top_left
        self.right, self.bottom = bottom_right


def rectangular_love(r1, r2):
    y_coord = (r1.bottom, r1.top, r2.bottom, r2.top)
    x_coord = (r1.left, r1.right, r2.left, r2.right)
    return _has_overlap(*y_coord) and _has_overlap(*x_coord)


def _has_overlap(a_min, a_max, b_min, b_max):
    if (a_min > b_max) or (a_max < b_min):
        return False
    return True

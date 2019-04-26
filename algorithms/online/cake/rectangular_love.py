class Rectangle:
    def __init__(self, top_left, bottom_right):
        self.left, self.top = top_left
        self.right, self.bottom = bottom_right


def rectangular_love(r1, r2):
    y_coords = (r1.bottom, r1.top, r2.bottom, r2.top)
    x_coords = (r1.left, r1.right, r2.left, r2.right)
    return has_overlap(*y_coords) and has_overlap(*x_coords)


def has_overlap(a_min, a_max, b_min, b_max):
    if (a_min > b_max) or (a_max < b_min):
        return False
    return True

class Rectangle(object):

    def __init__(self, top_left, bottom_right):
        self.left, self.top = top_left
        self.right, self.bottom = bottom_right


def rectangular_love(r1, r2):
    if not has_overlap(r1.bottom, r1.top, r2.bottom, r2.top):
        return False
    if not has_overlap(r1.left, r1.right, r2.left, r2.right):
        return False
    return True


def has_overlap(a_min, a_max, b_min, b_max):
    if (a_min > b_max) or (a_max < b_min):
        return False
    return True

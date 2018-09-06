class Rectangle(object):

    def __init__(self, top_left, bottom_right):
        self.left, self.top = top_left
        self.right, self.bottom = bottom_right


def rectangular_love(r1, r2):
    if not has_overlap(r1.top, r1.bottom, r2.top, r2.bottom):
        return False
    if not has_overlap(r1.left, r1.right, r2.left, r2.right):
        return False
    return True


def has_overlap(l1_bound, r1_bound, l2_bound, r2_bound):
    if l1_bound < r1_bound < l2_bound < r2_bound:
        return False
    if l2_bound < r2_bound < l1_bound < r1_bound:
        return False
    return True

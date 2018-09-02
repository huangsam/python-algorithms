from online.codesignal.rotateImage import rotateImage


class TestRotateImage(object):

    def test_rotate_one(self):
        image = [
            [1],
        ]
        rotated = [
            [1],
        ]
        assert rotated == rotateImage(image)

    def test_rotate_two(self):
        image = [
            [1, 1],
            [2, 2],
        ]
        rotated = [
            [2, 1],
            [2, 1],
        ]
        assert rotated == rotateImage(image)

    def test_rotate_three(self):
        image = [
            [1, 1, 1],
            [2, 2, 2],
            [3, 3, 3],
        ]
        rotated = [
            [3, 2, 1],
            [3, 2, 1],
            [3, 2, 1],
        ]
        assert rotated == rotateImage(image)

    def test_rotate_five(self):
        image = [
            [1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3],
            [4, 4, 4, 4, 4],
            [5, 5, 5, 5, 5],
        ]
        rotated = [
            [5, 4, 3, 2, 1],
            [5, 4, 3, 2, 1],
            [5, 4, 3, 2, 1],
            [5, 4, 3, 2, 1],
            [5, 4, 3, 2, 1],
        ]
        assert rotated == rotateImage(image)

import pytest

from algorithms.online.codesignal.rotateImage import rotateImage


@pytest.mark.array
@pytest.mark.parametrize(
    "image",
    [
        [[1]],
        [[1, 2], [1, 2]],
        [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
        [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
        ],
        [
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
        ],
    ],
)  # fmt: skip
def test_rotate_image(image):
    rotated = rotateImage(image)
    ilen = len(image)
    for i in range(ilen):
        for j in range(ilen):
            assert image[i][j] == rotated[j][ilen - i - 1]

# http://www.cnblogs.com/zuoyuan/p/3783993.html
def largest_rect(histo):
    """Determine largest rectangle in a histogram.

    Args:
        histo (list): Each element indicates a height for one width.

    Returns:
        int: The maximum area found.
    """
    hlen = len(histo)
    positions, heights = [], []
    max_area = 0
    # build `heights`
    for h in range(hlen):
        height = histo[h]
        if len(heights) == 0 or height > heights[-1]:
            heights.append(height)
            positions.append(h)
        elif height < heights[-1]:
            last_position = 0
            while len(heights) > 0 and height < heights[-1]:
                last_position = positions.pop()
                tmp_area = heights.pop() * (h - last_position)
                if max_area < tmp_area:
                    max_area = tmp_area
            heights.append(height)
            positions.append(last_position)
        print(height, heights, positions)
    # process remainder of `heights`
    while len(heights) > 0:
        last_position = positions.pop()
        tmp_area = heights.pop() * (hlen - last_position)
        if max_area < tmp_area:
            max_area = tmp_area
    return max_area


def main():
    histo_1 = [1, 3, 5, 3, 0, 2, 6, 6, 1, 0, 3, 6]
    histo_2 = [1, 3, 5, 3, 2, 2, 3, 3, 1, 0, 3, 6]
    histo_3 = [1, 3, 2, 1, 2]
    assert 12 == largest_rect(histo_1)
    assert 14 == largest_rect(histo_2)
    assert 5 == largest_rect(histo_3)


if __name__ == '__main__':
    main()

# http://www.cnblogs.com/zuoyuan/p/3783993.html
def largest_rect(histo):
    """Determine largest rectangle in a histogram.

    Args:
        histo: Each element indicates a height for one width.

    Returns:
        The maximum area found.
    """
    positions, heights = [], []
    max_area = 0
    # build `heights`
    for i, h in enumerate(histo):
        if len(heights) == 0 or h > heights[-1]:
            heights.append(h)
            positions.append(i)
        elif h < heights[-1]:
            last_position = 0
            while len(heights) > 0 and h < heights[-1]:
                last_position = positions.pop()
                tmp_area = heights.pop() * (i - last_position)
                if max_area < tmp_area:
                    max_area = tmp_area
            heights.append(h)
            positions.append(last_position)
    # process remainder of `heights`
    while len(heights) > 0:
        last_position = positions.pop()
        tmp_area = heights.pop() * (len(histo) - last_position)
        if max_area < tmp_area:
            max_area = tmp_area
    return max_area

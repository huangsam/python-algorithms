def max_weight_path(triangle: list[list[int]]):
    height = len(triangle)
    prev_val = None
    for i in range(height - 1, 0, -1):
        sums = []
        above = triangle[i - 1]
        row = prev_val or triangle[i]
        row_len = len(row)
        for j in range(row_len - 1):
            row_val = max(row[j] + above[j], row[j + 1] + above[j])
            sums.append(row_val)
        prev_val = sums
    if prev_val is None:
        raise RuntimeError("This should not happen")
    return prev_val[0]

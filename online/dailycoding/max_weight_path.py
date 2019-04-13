def max_weight_path(triangle):
    height = len(triangle)
    i = height - 1
    prev_val = None
    while i > 0:
        sums = []
        above = triangle[i - 1]
        row = prev_val or triangle[i]
        row_len = len(row)
        j = 0
        while j < row_len - 1:
            row_val = max(row[j] + above[j], row[j + 1] + above[j])
            sums.append(row_val)
            j += 1
        prev_val = sums
        i -= 1
    return prev_val[0]

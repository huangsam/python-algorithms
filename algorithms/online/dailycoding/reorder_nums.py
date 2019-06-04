def reorder_nums(jumbled):
    greater_count = sum([1 for ch in jumbled if ch == "+"])
    first_num = len(jumbled) - greater_count - 1
    greater_num = first_num + 1
    lesser_num = first_num - 1
    result = [first_num]
    for ch in jumbled[1:]:
        if ch == "+":
            result.append(greater_num)
            greater_num += 1
        else:
            result.append(lesser_num)
            lesser_num -= 1
    return result

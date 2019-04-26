def common_elements(a1, a2, a3):
    new_a = get_common(a1, a2)
    return get_common(new_a, a3)


def get_common(a1, a2):
    i1, i2 = 0, 0
    result = []
    while i1 < len(a1) and i2 < len(a2):
        if a1[i1] == a2[i2]:
            if not result or a1[i1] != result[-1]:
                result.append(a1[i1])
            i1 += 1
            i2 += 1
        elif a1[i1] < a2[i2]:
            i1 += 1
        else:
            i2 += 1
    return result

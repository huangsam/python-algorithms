# https://www.geeksforgeeks.org/sort-array-according-order-defined-another-array/
def relative_sort(a1, a2):
    a1_set = get_count(a1)
    result = []
    for e in a2:
        if e in a1_set:
            result.extend([e] * a1_set[e])
            del a1_set[e]
    for k in sorted(a1_set.keys()):
        result.extend([k] * a1_set[k])
    return result


def get_count(a):
    result = {}
    for e in a:
        if e not in result:
            result[e] = 0
        result[e] += 1
    return result

def depth_sum(a, weight=1):
    sum = 0
    for el in a:
        if type(el) != list:
            sum += el * weight
        else:
            sum += depth_sum(el, weight + 1)
    return sum


def depth_sum_stack(a):
    sum = 0
    stack = [a, 1]
    while len(stack) > 0:
        cur_weight = stack.pop()
        cur_list = stack.pop()
        for el in cur_list:
            if type(el) != list:
                sum += el * cur_weight
            else:
                stack.append(el)
                stack.append(cur_weight + 1)
    return sum


depth_sum([[1, 1], 2, [1, 1]])
depth_sum_stack([[1, 1], 2, [1, 1]])

# https://www.geeksforgeeks.org/power-set/
def power_set(items):
    N = len(items)
    # run 2 ** N possible combinations
    for i in range(2 ** N):
        combo = []
        for j in range(N):
            # test bit j of value i
            if (i >> j) & 1 == 1:
                combo.append(items[j])
        yield combo

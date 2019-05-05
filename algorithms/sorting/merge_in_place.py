# https://www.geeksforgeeks.org/sorted-merge-one-array/
def merge_in_place(a, b):
    try:
        aind = a.index(None) - 1
    except ValueError:
        return a
    bind = len(b) - 1
    cind = len(a) - 1
    while bind >= 0:
        if aind >= 0 and a[aind] > b[bind]:
            a[cind] = a[aind]
            aind -= 1
        else:
            a[cind] = b[bind]
            bind -= 1
        cind -= 1

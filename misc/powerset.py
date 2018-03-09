import unittest


def get_all_subsets(remaining_list):
    pass


def get_powerset(some_list):
    """Returns all subsets of size 0 - len(some_list) for some_list"""
    if len(some_list) == 0:
        return [[]]

    subsets = []
    first_element = some_list[0]
    remaining_list = some_list[1:]
    # Strategy: get all the subsets of remaining_list. For each
    # of those subsets, a full subset list will contain both
    # the original subset as well as a version of the subset
    # that contains first_element
    for partial_subset in get_all_subsets(remaining_list):
        subsets.append(partial_subset)
        subsets.append(partial_subset[:] + [first_element])

    return subsets


def powerset(items):
    N = len(items)
    # enumerate the 2 ** N possible combinations
    for i in range(2 ** N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


class PowerTestCase(unittest.TestCase):
    def test_powerset(self):
        size = 15
        vals = tuple([val for val in range(size)])
        result = list(powerset(vals))
        self.assertEquals(len(result), 2**size)


if __name__ == '__main__':
    unittest.main()

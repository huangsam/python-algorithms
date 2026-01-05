from algorithms.online.exponent.longest_subseq_diff import longest_subseq_diff


def test_basic_case():
    nums = [1, 3, 5, 7]
    target = 4
    assert longest_subseq_diff(nums, target) == 2  # e.g., [1,3], [3,5], [5,7]


def test_all_elements_within_target():
    nums = [1, 2, 3]
    target = 5
    assert longest_subseq_diff(nums, target) == 3


def test_no_elements_within_target():
    nums = [1, 5, 10]
    target = 2
    assert longest_subseq_diff(nums, target) == 1


def test_empty_list():
    nums = []
    target = 5
    assert longest_subseq_diff(nums, target) == 0


def test_single_element():
    nums = [5]
    target = 10
    assert longest_subseq_diff(nums, target) == 1


def test_duplicates():
    nums = [2, 2, 2]
    target = 1
    assert longest_subseq_diff(nums, target) == 3


def test_large_target():
    nums = [1, 10, 100]
    target = 200
    assert longest_subseq_diff(nums, target) == 3


def test_small_target():
    nums = [1, 2, 3, 4, 5]
    target = 2
    assert longest_subseq_diff(nums, target) == 2  # e.g., [1,2], [2,3], etc.


def test_unsorted_input():
    nums = [5, 1, 3, 7]
    target = 4
    assert longest_subseq_diff(nums, target) == 2  # sorted: [1,3,5,7]


def test_negative_numbers():
    nums = [-5, -3, -1, 1]
    target = 3
    assert longest_subseq_diff(nums, target) == 2  # e.g., [-5,-3], [-3,-1], [-1,1]


def test_mixed_positive_negative():
    nums = [-10, 0, 10]
    target = 11
    assert longest_subseq_diff(nums, target) == 2  # e.g., [-10,0], [0,10]


def test_target_zero():
    nums = [1, 2, 3]
    target = 0
    assert longest_subseq_diff(nums, target) == 1  # difference must be < 0, impossible unless single element


def test_large_list():
    nums = list(range(100))
    target = 10
    assert longest_subseq_diff(nums, target) == 10  # 0 to 9, diff=9<10

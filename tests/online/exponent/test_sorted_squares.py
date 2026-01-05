from algorithms.online.exponent.sorted_squares import find_kth_squared_value, sorted_squares


class TestSortedSquares:
    def test_empty_list(self):
        assert sorted_squares([]) == []

    def test_single_element_zero(self):
        assert sorted_squares([0]) == [0]

    def test_single_element_negative(self):
        assert sorted_squares([-1]) == [1]

    def test_single_element_positive(self):
        assert sorted_squares([1]) == [1]

    def test_positive_numbers(self):
        assert sorted_squares([1, 2, 3]) == [1, 4, 9]

    def test_negative_numbers(self):
        assert sorted_squares([-3, -2, -1]) == [1, 4, 9]

    def test_mixed_numbers(self):
        assert sorted_squares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]

    def test_duplicates(self):
        assert sorted_squares([-2, -2, 1, 1]) == [1, 1, 4, 4]


class TestFindKthSquaredValue:
    def test_basic_case(self):
        nums = [-4, -1, 0, 3, 10]
        assert find_kth_squared_value(nums, 1) == 0
        assert find_kth_squared_value(nums, 2) == 1
        assert find_kth_squared_value(nums, 3) == 9
        assert find_kth_squared_value(nums, 4) == 16
        assert find_kth_squared_value(nums, 5) == 100

    def test_duplicates(self):
        nums = [-2, -2, 1, 1]
        assert find_kth_squared_value(nums, 1) == 1
        assert find_kth_squared_value(nums, 2) == 1
        assert find_kth_squared_value(nums, 3) == 4
        assert find_kth_squared_value(nums, 4) == 4

    def test_single_element(self):
        nums = [5]
        assert find_kth_squared_value(nums, 1) == 25

    def test_negative_only(self):
        nums = [-3, -2, -1]
        assert find_kth_squared_value(nums, 1) == 1
        assert find_kth_squared_value(nums, 2) == 4
        assert find_kth_squared_value(nums, 3) == 9

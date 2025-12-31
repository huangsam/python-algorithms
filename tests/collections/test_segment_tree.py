from algorithms.collections.segment_tree import SegmentTree


class TestSegmentTree:
    def test_build_and_query(self):
        arr = [1, 3, 5, 7, 9, 11]
        st = SegmentTree(arr)
        # Query whole range
        result = st.query_range(0, 5)
        assert result.sum_val == sum(arr)
        assert result.min_val == min(arr)
        assert result.max_val == max(arr)
        assert result.gcd_val == 1  # gcd of 1,3,5,7,9,11 is 1
        # Query subrange
        result = st.query_range(1, 3)
        assert result.sum_val == 3 + 5 + 7
        assert result.min_val == 3
        assert result.max_val == 7
        # Single element
        result = st.query_range(2, 2)
        assert result.sum_val == 5
        assert result.min_val == 5
        assert result.max_val == 5

    def test_update(self):
        arr = [1, 3, 5, 7, 9, 11]
        st = SegmentTree(arr)
        # Update index 2 to 10
        st.update_val(2, 10)
        result = st.query_range(0, 5)
        assert result.sum_val == 1 + 3 + 10 + 7 + 9 + 11
        result = st.query_range(2, 2)
        assert result.sum_val == 10
        assert result.min_val == 10
        assert result.max_val == 10

    def test_edge_cases(self):
        arr = [5]
        st = SegmentTree(arr)
        result = st.query_range(0, 0)
        assert result.sum_val == 5
        assert result.min_val == 5
        assert result.max_val == 5
        st.update_val(0, 10)
        result = st.query_range(0, 0)
        assert result.sum_val == 10
        assert result.min_val == 10
        assert result.max_val == 10

    def test_empty_range(self):
        arr = [1, 2, 3]
        st = SegmentTree(arr)
        # Query invalid range should return neutral values
        result = st.query_range(1, 0)
        assert result.sum_val == 0
        assert result.min_val == float("inf")
        assert result.max_val == float("-inf")
        assert result.gcd_val == 0

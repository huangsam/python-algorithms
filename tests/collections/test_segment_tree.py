from algorithms.collections.segment_tree import SegmentTree


class TestSegmentTree:
    def test_build_and_query(self):
        arr = [1, 3, 5, 7, 9, 11]
        st = SegmentTree(arr)
        # Query whole range
        assert st.query_range(0, 5) == sum(arr)
        # Query subrange
        assert st.query_range(1, 3) == 3 + 5 + 7
        # Single element
        assert st.query_range(2, 2) == 5

    def test_update(self):
        arr = [1, 3, 5, 7, 9, 11]
        st = SegmentTree(arr)
        # Update index 2 to 10
        st.update_val(2, 10)
        assert st.query_range(0, 5) == 1 + 3 + 10 + 7 + 9 + 11
        assert st.query_range(2, 2) == 10

    def test_edge_cases(self):
        arr = [5]
        st = SegmentTree(arr)
        assert st.query_range(0, 0) == 5
        st.update_val(0, 10)
        assert st.query_range(0, 0) == 10

    def test_empty_range(self):
        arr = [1, 2, 3]
        st = SegmentTree(arr)
        # Query invalid range should return 0
        assert st.query_range(1, 0) == 0

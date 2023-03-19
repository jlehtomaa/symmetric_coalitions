from symmetric_coalitions.utils import integer_partition, sorted_integer_partition

def test_integer_partition():
    """Test that the algorithm finds the correct partitionings."""

    assert [*integer_partition(0)] == [[0]]
    assert [*integer_partition(1)] == [[1]]

    three_player_list = [[1,1,1], [1,2], [3]]
    assert sorted([*integer_partition(3)]) == three_player_list

def test_sorted_integer_partition():
    """Test that the integer partition generator produces the right coalitions."""

    assert sorted_integer_partition(0) == [(0,)]
    assert sorted_integer_partition(1) == [(1,)]

    three_player_list = [(1,1,1), (2,1), (3,)]
    assert sorted_integer_partition(3) == three_player_list

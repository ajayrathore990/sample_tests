from gfg_list.majaority_element import majority_wins

def test_majority_wins_empty():
    result = majority_wins([])
    assert result == 0


def test_majority_wins_one():
    result = majority_wins([1,1,2,4,4,4,4,4])
    assert result == 4

def test_majority_wins_two():
    result = majority_wins([10,10,10,10,2,3])
    assert result == 10

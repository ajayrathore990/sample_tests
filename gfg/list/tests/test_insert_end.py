from gfg_list.insert_end import insert_at_end

def test_insert_end_empty_list():
    result = insert_at_end([],5)
    assert result == 0

def test_insert_end_one():
    result = insert_at_end([1,2,3],5)
    assert result == [1,2,3,5]

def test_insert_end_two():
    result = insert_at_end([10,11,12],15)
    assert result == [10,11,12,15]

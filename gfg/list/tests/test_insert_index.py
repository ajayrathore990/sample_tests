from gfg_list.insert_index import insert_at_index


def test_insert_index_empty():
    result = insert_at_index([],0,22)
    assert result == 0

def test_insert_index_out_of_range():
    result = insert_at_index([1,2,3],44,0)
    assert result == [1,2,3,0]

def test_insert_index_one():
    result = insert_at_index([1,2,3],2,22)
    assert result == [1,2,22,3]

def test_insert_index_two():
    result = insert_at_index([3,2,1],0,0)
    assert result == [0,3,2,1]

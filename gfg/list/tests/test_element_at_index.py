from gfg_list.element_at_index import get_by_index

def test_get_by_index_empty():
    result = get_by_index([],2) 
    assert result == 0

def test_get_by_index_out_of_index():
    result = get_by_index([1,2,3],9) 
    assert result == 0

def test_get_by_index_one():
    result = get_by_index([1,2,3],2) 
    assert result == 3


def test_get_by_index_two():
    result = get_by_index([10,20,30,40,50],1) 
    assert result == 20

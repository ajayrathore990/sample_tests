from gfg_list.update_at_index import update_array

def test_update_array_empty():
    result = update_array([],2,1) 
    assert result == 0

def test_update_array_out_of_range():
    result = update_array([1,2,3],0,5) 
    assert result == 0

def test_update_array_one():
    result = update_array([1,2,3],0,0) 
    assert result == [0,2,3]

def test_update_array_two():
    result = update_array([10,20,30,40,50],22,2) 
    assert result == [10,20,22,40,50]

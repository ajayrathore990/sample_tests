from gfg_list.delete_and_shift import delete_from_array

def test_delete_from_array_empty():
    result = delete_from_array([],2) 
    assert result == 0

def test_delete_from_array_out_of_range():
    result = delete_from_array([1,2,3],5) 
    assert result == 0

def test_delete_from_array_one():
    result = delete_from_array([1,2,3],0) 
    assert result == [2,3]

def test_delete_from_array_two():
    result = delete_from_array([10,20,30,40,50],2) 
    assert result == [10,20,40,50]

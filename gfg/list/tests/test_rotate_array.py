from gfg_list.rotate_array import rotate_arr

def test_rotate_arr_empty():
    result = rotate_arr([],3) 
    assert result == 0

def test_rotate_arr_out_of_range():
    result = rotate_arr([1,2,3,4,5,6,7],9) 
    assert result == 0

def test_rotate_arr_one():
    result = rotate_arr([1,2,3,4,5,6,7],2) 
    assert result == [3,4,5,6,7,1,2]

def test_rotate_arr_two():
    result = rotate_arr([1,2,3,4,5,6,7],6) 
    assert result == [7,1,2,3,4,5,6]

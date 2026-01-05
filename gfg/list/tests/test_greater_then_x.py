from gfg_list.count_greater_then_x import greater_then_x

def test_greater_then_x_empty():
    result = greater_then_x([],2) 
    assert result == 0

def test_greater_then_x_out_of_range():
    result = greater_then_x([1,2,3],5) 
    assert result == 3

def test_greater_then_x_one():
    result = greater_then_x([1,2,3,4,4,4,4],4) 
    assert result == 3

def test_greater_then_x_two():
    result = greater_then_x([10,20,30,40,50],30) 
    assert result == 2

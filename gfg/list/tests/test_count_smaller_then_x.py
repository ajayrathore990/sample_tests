from gfg_list.count_smaller_then_x import smaller_then_x

def test_smaller_then_x_empty():
    result = smaller_then_x([],2) 
    assert result == 0

def test_smaller_then_x_out_of_range():
    result = smaller_then_x([1,2,3],5) 
    assert result == 0

def test_smaller_then_x_one():
    result = smaller_then_x([1,2,3,4,4,4,4],4) 
    assert result == 0

def test_smaller_then_x_two():
    result = smaller_then_x([10,20,30,40,50],30) 
    assert result == 2

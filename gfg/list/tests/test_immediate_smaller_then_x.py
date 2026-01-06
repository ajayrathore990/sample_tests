from gfg_list.immediate_smaller_then_x import immediate_smaller

def test_immediate_smaller_then_x_empty():
    result = immediate_smaller([],2) 
    assert result == 0

def test_immediate_smaller_out_of_range():
    result = immediate_smaller([1,2,3],5) 
    assert result == 0

def test_immediate_smaller_then_x_one():
    result = immediate_smaller([1,2,3,4,5,6,7],4) 
    assert result == 3

def test_immediate_smaller_then_x_two():
    result = immediate_smaller([10,20,30,40,50],35) 
    assert result == 30

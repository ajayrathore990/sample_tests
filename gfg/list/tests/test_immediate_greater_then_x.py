from gfg_list.immediate_greater_then_x import immediate_greater

def test_immediate_greater_empty():
    result = immediate_greater([],2) 
    assert result == 0

def test_immediate_greater_x_out_of_range():
    result = immediate_greater([1,2,3],5) 
    assert result == 0

def test_immediate_greater_one():
    result = immediate_greater([10,20,30,40,50,60],40) 
    assert result == 50

def test_immediate_greater_x_two():
    result = immediate_greater([11,22,33,44,55],30) 
    assert result == 33

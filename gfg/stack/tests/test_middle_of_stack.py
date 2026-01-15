from gfg_stack.middle_of_stack import middle_stack

def test_middle_stack_empty():
    result  = middle_stack([])
    assert result ==0

def test_middle_stack_one_element():
    result  = middle_stack([44])
    assert result == 44

def test_middle_stack_two_element():
    result  = middle_stack([11,22])
    assert result ==22

def test_middle_stack_one():
    result  = middle_stack([1,22,44])
    assert result ==22
    
def test_middle_stack_two():
    result  = middle_stack([1,2,3,4,5,6,7,8,9])
    assert result ==5

def test_middle_stack_three():
    result  = middle_stack([1,2,3,4,5,6,7,8,9])
    assert result ==5

from gfg_stack.reverse_stack_using_stack import reverse_stack

def test_reverse_stack_empty():
    result = reverse_stack([]) 
    assert result == []

def test_reverse_stack_single():
    result = reverse_stack([1]) 
    assert result == [1]

def test_reverse_stack_one():
    result = reverse_stack([1,2,3]) 
    assert result == [3,2,1]

def test_reverse_stack_two():
    result = reverse_stack([11,26,34]) 
    assert result == [34,26,11]

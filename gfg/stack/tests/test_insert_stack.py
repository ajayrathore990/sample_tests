from gfg_stack.insert_stack import insert_in_stack

def test_insert_in_stack_empty():
    result = insert_in_stack([],2) 
    assert result == [2]

def test_insert_in_stack_one():
    result = insert_in_stack([1,2,3],5) 
    assert result == [1,2,3,5]

def test_insert_in_stack_two():
    result = insert_in_stack([45,36,28,19],4) 
    assert result == [45,36,28,19,4]

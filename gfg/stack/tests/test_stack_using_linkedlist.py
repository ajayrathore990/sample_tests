import pytest 

from gfg_stack.stack_using_linkedlist import Stack

@pytest.fixture
def my_stack():
    s = Stack() 
    return s

def test_using_linked_list_data(my_stack):
    s = my_stack        
    s.push(22)
    assert s.peek() == 22
    assert s.size == 1

def test_using_linked_list_empty(my_stack):
    s = my_stack        
    s.push(22)
    s.pop()
    assert s.size == 0

import pytest
from gfg_stack.operation_on_stack import Stack

@pytest.fixture
def my_stack():
    s = Stack() 
    return s

def test_is_empty_one(my_stack):
    s = my_stack        
    s.insert(22)
    assert not s.is_empty()

def test_is_empty_two(my_stack):
    s = my_stack
    assert  s.is_empty()
    
def test_pop_one(my_stack):
    s = my_stack
    assert s.pop() == 0
    
def test_pop_two(my_stack):
    s = my_stack
    s.insert(10)
    assert s.pop() == 0
    
def test_top_element_one(my_stack):
    s = my_stack
    s.insert(10)
    assert s.top_element() == 10
    
def test_top_element_two(my_stack):
    s = my_stack
    assert s.top_element() == 0
    
def test_check_element_one(my_stack):
    s = my_stack
    s.insert(10)
    s.check_element(10)
    assert s.check_element(10)
    
def test_check_element_two(my_stack):
    s =my_stack
    s.insert(10)
    assert not s.check_element(20)

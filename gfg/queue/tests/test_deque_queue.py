import pytest
from gfg_queue.queue_deque import Deque_queue

@pytest.fixture
def my_queue():
    object = Deque_queue()
    return object

def test_queue_is_empty_one(my_queue):
    s = my_queue        
    assert s.is_empty() == True
    
def test_queue_is_empty_two(my_queue):
    s = my_queue        
    s.insert(1)
    assert s.is_empty() == False

def test_queue_insert(my_queue):
    s = my_queue        
    assert s.insert(1) == 1
    assert s.insert(2) == 2

def test_queue_remove(my_queue):
    s = my_queue
    s.insert(1)
    assert s.remove() == 1

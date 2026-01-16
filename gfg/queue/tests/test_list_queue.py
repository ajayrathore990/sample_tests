import pytest 
from gfg_queue.list_queue import List_queue


@pytest.fixture
def my_queue():
    object = List_queue()
    return object

def test_list_queue_is_empty_one(my_queue):
    s = my_queue        
    assert s.is_empty() == True

def test_list_queue_is_empty_two(my_queue):
    s = my_queue        
    s.insert(1)
    assert s.is_empty() == False

def test_list_queue_insert(my_queue):
    s = my_queue
    assert s.insert(2) == 2

def test_list_queue_remove_one(my_queue):
    s = my_queue
    assert s.remove() == 0

def test_list_queue_remove_two(my_queue):
    s = my_queue
    s.insert(1)
    assert s.remove() == 1

def test_list_queue_get_front(my_queue):
    s = my_queue
    s.insert(1)
    assert s.get_front() == 1

def test_list_queue_get_rare(my_queue):
    s = my_queue
    s.insert(1)
    assert s.get_rear() == 1

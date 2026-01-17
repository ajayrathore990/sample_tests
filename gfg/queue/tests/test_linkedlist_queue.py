import pytest
from gfg_queue.linkedlist_queue import Queue

@pytest.fixture
def my_queue():
    object = Queue()
    object.enqueue(10)
    return object

def test_linked_list_queue_one(my_queue):
    obj = my_queue
    assert obj.is_empty() == False
    assert obj.size == 1

def test_linked_list_queue_get_data_one(my_queue):
    obj = my_queue
    assert obj.get_front() == 10
    assert obj.get_rear() == 10

def test_linked_list_queue_two(my_queue):
    obj = my_queue
    obj.enqueue(20)
    assert obj.is_empty() == False
    assert obj.size == 2

def test_linked_list_queue_get_data_two(my_queue):
    obj = my_queue
    obj.enqueue(20)
    assert obj.get_front() == 10
    assert obj.get_rear() == 20
    
def test_linked_list_queue_three(my_queue):
    obj = my_queue
    obj.enqueue(20)
    obj.enqueue(30)
    obj.dequeue()
    assert obj.is_empty() == False
    assert obj.size == 2

def test_linked_list_queue_get_data_three(my_queue):
    obj = my_queue
    obj.enqueue(20)
    obj.enqueue(30)
    assert obj.get_front() == 10
    assert obj.get_rear() == 30
import pytest
from gfg_queue.circular_queue import Circular_List_Queue

@pytest.fixture
def my_queue():
    obj = Circular_List_Queue(4)
    return obj

def test_circuler_list_queue_check_size(my_queue):
    obj= my_queue
    assert obj.size ==0
    assert obj.is_empty() ==True

def test_circuler_list_queue_enqueue_one(my_queue):
    obj= my_queue
    obj.enqueue(21)
    assert obj.size ==1
    assert obj.is_empty() ==False

def test_circuler_list_queue_enqueue(my_queue):
    obj= my_queue
    obj.enqueue(21)
    obj.enqueue(22)
    assert obj.size ==2
    assert obj.is_empty() ==False

def test_circuler_list_queue_dequeue(my_queue):
    obj= my_queue
    obj.enqueue(21)
    obj.enqueue(22)
    obj.dequeue()
    assert obj.size ==1
    assert obj.is_empty() ==False

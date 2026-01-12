from gfg_stack.stack_using_array import Stack

def test_insert_in_stack_one():
    obj = Stack()
    obj.insert(1)
    obj.insert(2)
    assert obj.show() == [1,2]

def test_insert_in_stack_two():
    obj = Stack()
    obj.insert(20)
    obj.insert(23)
    assert obj.show() == [20,23]

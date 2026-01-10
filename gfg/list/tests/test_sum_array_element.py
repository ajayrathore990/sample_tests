from gfg_list.sum_array_element import sum_element

def test_sum_element_empty():
    result = sum_element([]) 
    assert result == 0

def test_sum_element_single_element():
    result = sum_element([3]) 
    assert result == 3

def test_sum_element_one():
    result = sum_element([1,2,3,4,5,6,7]) 
    assert result == 28

def test_sum_element_two():
    result = sum_element([1,2,3,4,5]) 
    assert result == 15

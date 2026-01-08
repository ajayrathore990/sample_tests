from gfg_list.max_and_min import max_min

def test_min_max_empty():
    result = max_min([]) 
    assert result == 0

def test_min_max_less_input():
    result = max_min([1]) 
    assert result == 0

def test_min_max_one():
    result = max_min([10,20,30,40]) 
    assert result == (40,10)

def test_min_max_two():
    result = max_min([33,54,56,23,98]) 
    assert result == (98,23)

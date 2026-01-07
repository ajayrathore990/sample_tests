from gfg_list.is_array_sorted import sored_array

def test_sored_array_empty():
    result = sored_array([]) 
    assert result == True

def test_sored_array_single_input():
    result = sored_array([1]) 
    assert result == True

def test_sored_array_one():
    result = sored_array([1,30,40,100]) 
    assert result == True

def test_sored_array_two():
    result = sored_array([98,87,72,61,52,32]) 
    assert result == True

def test_sored_array_three():
    result = sored_array([1,30,40,34]) 
    assert result == False

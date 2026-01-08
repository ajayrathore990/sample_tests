from gfg_list.mean_median_array import mean_median

def test_mean_median_empty():
    result = mean_median([]) 
    assert result == (0,0)

def test_mean_median_single_eement():
    result = mean_median([7]) 
    assert result == (7,7)

def test_mean_median_one():
    result = mean_median([1,2,3,4,5,6,7]) 
    assert result == (4,4)

def test_mean_median_two():
    result = mean_median([5,6,7]) 
    assert result == (6,6)

from gfg_list.reverse_array import reverse_list1,reverse_list2

def test_reverse_array_empty():
    result1 = reverse_list1([]) 
    result2 = reverse_list2([]) 
    assert result1 == 0
    assert result2 == 0

def test_reverse_array_one():
    result1 = reverse_list1([1,2,3,5,6]) 
    result2 = reverse_list2([1,2,3,5,6]) 
    assert result1 == [6,5,3,2,1]
    assert result2 == [6,5,3,2,1]


def test_reverse_array_one():
    result1 = reverse_list1([10,20,30]) 
    result2 = reverse_list2([10,20,30]) 
    assert result1 == [30,20,10]
    assert result2 == [30,20,10]

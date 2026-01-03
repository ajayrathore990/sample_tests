
from gfg_strings.reverse_string import string_reverse_one,string_reverse_two

def test_reverse_string_empty():
    result = string_reverse_one('')
    assert result == ''

def test_reverse_string_one():
    result_one = string_reverse_one('dcba')
    result_two = string_reverse_two('dcba')
    assert result_one == result_two == 'abcd'

    
def test_reverse_string_two():
    result_one = string_reverse_one('xyz')
    result_two = string_reverse_one('xyz')
    assert result_one == result_two == 'zyx'
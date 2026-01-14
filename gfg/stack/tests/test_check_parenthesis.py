from gfg_stack.stack_using_linkedlist import Stack

from gfg_stack.parenthesis_check import check_parenthesis

def test_check_string_one():
    result = check_parenthesis('[()]')
    assert result == True
    
def test_check_string_two():
    result = check_parenthesis('[)]')
    assert result == False
    
def test_check_string_three():
    result = check_parenthesis('((())')
    assert result == False
    
def test_check_string_four():
    result = check_parenthesis('([)]')
    assert result == False
    
def test_check_string_five():
    result = check_parenthesis('{}([()])')
    assert result == True
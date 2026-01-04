from gfg_strings.uppercase_string import uppercase

def test_uppercase_empty_string():
    result = uppercase('')
    assert result == ''

def test_uppercase_one():
    result = uppercase('Geeks')
    assert result == 'GEEKS'

def test_uppercase_two():
    result = uppercase('for')
    assert result == 'FOR'

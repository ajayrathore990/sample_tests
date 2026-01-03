from gfg_strings.string_validation import valid_string

def test_empty_valid_string():
    result = valid_string('')
    assert not result

def test_valid_string_one():
    result = valid_string('eHello123@')
    assert result

def test_valid_string_two():
    result = valid_string('hella')
    assert not result
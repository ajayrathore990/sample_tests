from gfg_strings.panagram_check import valid_panagram

def test_panagram_empty_string():
    result = valid_panagram('')
    assert not result 

def test_panagram_less_then_26_char():
    result = valid_panagram('abcdefghijklmnop')
    assert not result 

def test_panagram_one():
    result = valid_panagram('abcdefghijklmnopqrstuvwxyz')
    assert result

def test_panagram_two():
    result = valid_panagram('Heavyduty')
    assert not result
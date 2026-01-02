from gfg_strings.missing_char_panagram import miss_char_panagram


def test_missing_char_panagram_empty_string():
    result =miss_char_panagram('')
    assert not result

def test_missing_char_panagram_one():
    result =miss_char_panagram('abcdefghijlmnopqrstuvwxyz')
    assert result == 'k'

def test_missing_char_panagram_two():
    result =miss_char_panagram('abcdefhijklmnopqrstuvwxyz')
    assert result == 'g'

def test_missing_char_panagram_three():
    result =miss_char_panagram('abcdefghijklmnopqrsuvwxyz')
    assert result == 't'



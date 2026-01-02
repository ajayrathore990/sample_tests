from gfg_strings.lowercase_string import lowercase

def test_lowercase_empty_string():
    result  = lowercase('')
    assert result == ''

def test_lowercase_one():
    result  = lowercase('Geeks')
    assert result =='geeks'

def test_lowercase_two():
    result  = lowercase('For')
    assert result == 'for'
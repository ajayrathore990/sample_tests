from gfg_strings.anagram_string import is_anagram

def test_is_anagram_empty():
    result = is_anagram('','')
    assert result

def test_is_anagram_one():
    result = is_anagram('ab cdaz','zaab dc')
    assert result

def test_is_anagram_two():
    result = is_anagram('allergy','allergic')
    assert not result

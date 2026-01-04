from gfg_strings.vowels_in_string import vowels_string


def test_vowels_empty_string():
    result = vowels_string('')
    assert result == 0

def test_vowels_string1():
    result = vowels_string("geeks")
    assert result == 2


def test_vowels_string2():
    result = vowels_string("world")
    assert result == 1

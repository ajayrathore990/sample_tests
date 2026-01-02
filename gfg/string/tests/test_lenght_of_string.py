from gfg_strings.length_of_string import lenght_string


def test_length_empty_string():
    result = lenght_string('')
    assert result == 0

def test_length_of_string1():
    result = lenght_string("Geeks")
    assert result == 5


def test_length_of_string2():
    result = lenght_string("startcode")
    assert result == 9

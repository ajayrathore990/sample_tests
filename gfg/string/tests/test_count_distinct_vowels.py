from gfg_strings.count_distinct_vowels_string import distinct_vowels


def test_distinct_vowels_empty_string():
    result = distinct_vowels('')
    assert result == 0

def test_distinct_vowels_1():
    result = distinct_vowels("geeks")
    assert result == 1


def test_distinct_vowels_2():
    result = distinct_vowels("world")
    assert result == 1

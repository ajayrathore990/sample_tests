from gfg_strings.count_words_string import count_words

def test_count_words_empty_string():
    result = count_words('')
    assert result == 0

def test_count_words1():
    result = count_words('Geeks')
    assert result == 1

def test_count_words2():
    result = count_words('World is Hello')
    assert result == 3



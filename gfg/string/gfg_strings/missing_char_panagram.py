def miss_char_panagram(string):
    if string == '':
        return False
    
    counter = []
    for i in string:
        value = ord(i)
        counter.append(value)
    miss_value = 2847 - sum(counter)

    return chr(miss_value)


def vowels_string(string):
    if string == '':
        return 0
    counter = 0
    for i in string:
        if i in ["a", "e", "i", "o", "u"]:
            counter = counter + 1
    return counter

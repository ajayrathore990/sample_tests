def distinct_vowels(string):
    if string == '':
        return 0
    for i in string:
        if i in ["a", "e", "i", "o", "u"]:
            my_set = set()
            my_set.add(i)
            counter = len(my_set)
    return counter

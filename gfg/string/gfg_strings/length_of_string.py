"""Lenth of the string"""


def lenght_string(string):
    if string == '':
        return 0    
    counter = 0
    formated_string = "".join(string.strip())
    for i in formated_string:
        counter = counter + 1
    return counter

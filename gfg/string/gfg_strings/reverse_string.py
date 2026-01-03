def string_reverse_one(string):
    if string== '':
        return ''

    return string[::-1]


def string_reverse_two(string):
    reverse = ""
    for ch in string:
        reverse = ch + reverse
    return  reverse


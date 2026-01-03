def valid_string(string):
    if string == '':
        return False
    upper = any(char.isupper() for char in string)
    lower = any(char.islower() for char in string)
    digit = any(char.isdigit() for char in string)
    alpha = any(char.isalpha() for char in string)

    if upper and lower and digit and alpha:
        return True
    else:
        return False

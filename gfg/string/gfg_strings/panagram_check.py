from string import ascii_lowercase

def valid_panagram(string):
    if string == '':
        return False
    
    for ch in ascii_lowercase:
        found = False
        
        for i in range(len(string)):
            if ch == (string[i].lower()):
                found = True
                break
        
        if found == False:
            return False
    return True
    

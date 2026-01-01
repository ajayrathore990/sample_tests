def is_anagram(string_a,string_b):
    if string_a == string_b == '':
        return True
    
    if len(string_a)==len(string_b):
        if sorted(string_a)==sorted(string_b):
            return True
        else: 
            return False
    else:
        return False


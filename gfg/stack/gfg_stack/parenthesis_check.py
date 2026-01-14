def is_match(v1,v2):
    if v1 == '['and v2 ==']' or \
        v1 == '{'and v2 =='}' or \
        v1 == '('and v2 ==')':
        return True
    else:
        return False

def check_parenthesis(string):
    stake =[]
    for i in string:
        if i in ('[','{','('):
            stake.append(i)
        else:
            if not stake:
                return False
            elif is_match(stake[-1],i) == False:
                return False
            else:
                stake.pop()
    if stake:
        return False
    else:
        return True
    
v= check_parenthesis('[()]')
print(v)
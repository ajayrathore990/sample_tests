def middle_stack(stack):
    len_of_stake = len(stack)
    if len_of_stake == 0:
        return 0
    
    if len_of_stake == 1:
        return stack[0]
    
    if len_of_stake==2:
        return stack[-1]
    if len_of_stake%2 ==0:
        return stack[int(len_of_stake/2)-1 ]
    else:
        return  stack[int(len_of_stake/2)]


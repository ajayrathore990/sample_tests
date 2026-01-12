def reverse_stack(stack):
    if stack==[]:
        return []
    if len(stack)== 1:
        return stack
    start = 0
    end= len(stack) +1
    new_stack=[]
    while start<= end:
        last_element= stack.pop()
        new_stack.append(last_element)
        start = start +1
        end = end-1
    return new_stack

print(reverse_stack([3,4,5]))

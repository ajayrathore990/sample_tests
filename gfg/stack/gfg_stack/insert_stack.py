def insert_in_stack(stack, item):
    if stack ==[]:
        return [item]
    stack.append(item)
    return stack

print(insert_in_stack([],4))

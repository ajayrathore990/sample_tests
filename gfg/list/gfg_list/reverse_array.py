def reverse_list1(list):
    if list ==[]:
        return 0
    return list[::-1]

def reverse_list2(list):
    if list ==[]:
        return 0
    new_list = []
    for i in list:
        new_list.insert(0,i)
    return new_list



def update_array(list,n, index):
    if list == []:
        return 0
    try:
        list[index] = n
    except IndexError as e:
        return 0
    return list 

#print(update_array([1,2],44,1))
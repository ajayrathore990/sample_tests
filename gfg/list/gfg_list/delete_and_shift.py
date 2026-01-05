def delete_from_array(list, index):
    if list == []:
        return 0
    try:
        del list[index]
    except IndexError as e:
        return 0
    return list 

print(delete_from_array([1,2,3],3))
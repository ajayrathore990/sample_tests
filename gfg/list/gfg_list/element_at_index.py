def get_by_index(list,index):
    try:
        if list ==[]:
            return 0
        result = list[index]
        return result
    except IndexError as e:
        return 0
    

print(get_by_index([1,2,3],5))
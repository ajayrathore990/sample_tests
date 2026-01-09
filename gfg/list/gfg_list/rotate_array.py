def rotate_arr(list, n):
    if list ==[]:
        return 0
    if n in list:
        return list[list.index(n+1):] + list[:list.index(n+1)]
    else:
        return 0
    

    
print(rotate_arr([1,2,3,4,5,6,7],10))
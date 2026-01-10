def sum_element(list):
    if list ==[]:
        return 0
    if len(list)==1:
        return list[0]
    count =0
    for i in list:
        count = count + i
    return count

print(sum_element([3,2,1,4]))
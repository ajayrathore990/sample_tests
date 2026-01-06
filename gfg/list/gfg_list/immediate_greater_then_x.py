def immediate_greater(list,x):
    if list == []:
        return 0
    if x < max(list) and  x > min(list):
        new_list = []
        try:
            for i in list:
                if i >x:
                    new_list.append(i)
            return min(new_list)
        except ValueError as e:
            return 0
    return 0


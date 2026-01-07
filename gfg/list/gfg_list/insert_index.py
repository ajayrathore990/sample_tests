def insert_at_index(list,item,index):
    try:
        if list == []:
            return 0
        list.insert(item,index)
        return list
    except IndexError as e:
        return 0


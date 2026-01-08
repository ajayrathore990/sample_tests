def majority_wins(list):
    if list == []:
        return 0
    dict = {}
    for i in list:
        value = list.count(i)
        dict[value] = i
    return dict[max(dict.keys())]


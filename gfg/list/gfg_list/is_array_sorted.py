def sored_array(list):
    if sorted(list) == list or sorted(list,reverse=True) == list:
        return True
    else:
        return False

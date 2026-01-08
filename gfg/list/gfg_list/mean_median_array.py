def mean_median(list):
    if list== []:
        return 0,0
    if len(list)==1:
        mean,median = list[0],list[0]
        return mean,median
    mean = sum(list)/len(list)
    median = sum(list)/len(list)
    return int(mean),int(median)

def split(number_list, parts):
    newarr = []
    temparr = []
    x = 0

    for val in number_list:
        if x < parts:
            temparr.append(val)
            x += 1
        if x >= parts:
            newarr.append(temparr)
            temparr = []
            x = 0

    if len(temparr) > 0:
        newarr.append(temparr)

    return newarr
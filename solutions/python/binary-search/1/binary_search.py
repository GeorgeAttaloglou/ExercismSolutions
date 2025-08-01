def find(search_list, value):
    search_list.sort()
    index = 0
    
    if len(search_list) == 0 or value not in search_list:
        raise ValueError("value not in array")

    for number in search_list:
        if search_list[index] == value:
            return index
        else:
            index += 1
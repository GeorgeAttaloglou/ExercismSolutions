
def find(search_list, value):
    if value not in search_list:
        raise ValueError("value not in array")

    index = len(search_list)//2
    if value < search_list[index]:
        return find(search_list[:index], value)
    if value > search_list[index]:
        return index + 1 + find(search_list[index+1:], value)
    return index

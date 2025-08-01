position_dictionary = {0:"wink", 1:"double blink", 2:"close your eyes", 3:"jump"}

def commands(binary_str: str) -> list:
    return_list = []
    flag = 0
    
    for digit in reversed(list(binary_str)):
        if digit == "1" and flag < len(position_dictionary):
            return_list.append(position_dictionary[flag])
        if flag >= len(position_dictionary):
            break
        flag += 1

    if binary_str[0] == "1":
        return list(reversed(return_list))

    return return_list

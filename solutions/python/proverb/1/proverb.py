import itertools

def proverb(*input_data: list, qualifier: str) -> list:

    listy = list(input_data)
    return_list = []
    return_list2 = []

    if len(listy) == 0:
        return listy

    if len(listy) == 1 and qualifier == None:
        return_list2.append("And all for the want of a " + listy[0] + ".")
        return return_list2
    elif len(listy) == 1 and qualifier:
        return_list2.append("And all for the want of a " + qualifier + " " + listy[0] + ".")
        return return_list2

    counter = 1
    for i in range(len(listy)-1):
        return_list.append("For want of a " + listy[counter - 1] + " the " + listy[counter] + " was lost.")
        counter += 1

    #TODO: make the last line be the "And all for the want of ..." line
    if qualifier == None:
        return_list.append("And all for the want of a " + listy[0] +".")
    else:
        return_list.append("And all for the want of a " + qualifier+ " " + listy[0] +".")

    return return_list

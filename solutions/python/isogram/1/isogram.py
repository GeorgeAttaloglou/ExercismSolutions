def is_isogram(string: str) -> bool:
    #if the current letter appears again in the word then return false
    #otherwise return true
    flag = True
    
    string = string.replace(' ','').replace('-','').lower()
    
    for i in range(0, len(string)):
        if string[i] in string[i+1:]:
            flag = False

    return flag

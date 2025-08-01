def is_isogram(string: str) -> bool:
    #sets cant have duplicates so compare the length of set to original string length
    
    string = string.replace(' ','').replace('-','').lower()

    return len(string) == len(set(string))

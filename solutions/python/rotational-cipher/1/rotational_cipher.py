def rotate(text, key):
    return_string = ""
    text = list(text)
    
    for char in text:
        if char.isalpha():
            if char.isupper():
                stayInAlpha = ord(char) + key
                if stayInAlpha > ord("Z"):
                    stayInAlpha -= 26
                finalLettet = chr(stayInAlpha)
                return_string += finalLettet
            elif char.islower():
                stayInAlpha = ord(char) + key
                if stayInAlpha > ord("z"):
                    stayInAlpha -= 26
                finalLettet = chr(stayInAlpha)
                return_string += finalLettet
        else :
            return_string += char
            
    return return_string

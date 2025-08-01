# this was an improvement made by chatgpt im not taking any credit for it

def rotate(text, key):
    result = []
    
    # Normalize the key to a range of 0-25
    key = key % 26
    
    for char in text:
        if char.isalpha():
            # Determine whether it's uppercase or lowercase
            ascii_offset = ord('A') if char.isupper() else ord('a')
            
            # Compute the new shifted character
            new_char = chr(ascii_offset + (ord(char) - ascii_offset + key) % 26)
            
            result.append(new_char)
        else:
            # Non-alphabetical characters remain unchanged
            result.append(char)
    
    return ''.join(result)

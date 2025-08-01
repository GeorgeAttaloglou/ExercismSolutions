alphabet = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'

reverse_alphabet_dict = {alphabet[i]: alphabet[-i-1] for i in range(len(alphabet))}

def encode(plain_text: str) -> str:
    plain_text_filtered = plain_text.lower()
    reversed_plain_text = ""

    #this is for keeping track of when a space will be added
    counter = 0
    for letter in plain_text_filtered:
        if letter == " " or letter == "," or letter == ".":
            continue
        elif letter in numbers:
            if counter < 5:
                reversed_plain_text += letter
                counter += 1
            else :
                counter = 0
                reversed_plain_text += " "
                reversed_plain_text += letter
                counter += 1
        else:
            if counter < 5 :
                reversed_plain_text += reverse_alphabet_dict[letter]
                counter += 1
            else:
                counter = 0
                reversed_plain_text += " "
                reversed_plain_text += reverse_alphabet_dict[letter]
                counter += 1

    return reversed_plain_text


def decode(ciphered_text):
    decoded_text = ""
    
    for letter in ciphered_text:
        if letter == " ":
            continue
        elif letter in numbers:
            decoded_text += letter
        else:
            for key, value in reverse_alphabet_dict.items():
                if letter == value:
                    decoded_text += key
    return decoded_text
            

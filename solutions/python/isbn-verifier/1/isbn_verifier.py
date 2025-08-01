accepted_characters = list("0123456789X")

def is_valid(isbn: str) -> bool:

    isbn_filtered = isbn.replace("-","")
    
    if len(isbn_filtered) != 10:
        return False
    
    isbn = list(isbn_filtered)
    filtered_isbn = []

    for character in isbn:
        if character in accepted_characters:
            filtered_isbn.append(character)
        else:
            return False

    if "X" in filtered_isbn and filtered_isbn[-1] != "X":
        return False

    result = 0
    integer_counter = 10
    for character in filtered_isbn:
        if character == "X":
            result += 10 * integer_counter
            integer_counter -= 1
        else:
            result += int(character) * integer_counter
            integer_counter -= 1

    return result % 11 == 0

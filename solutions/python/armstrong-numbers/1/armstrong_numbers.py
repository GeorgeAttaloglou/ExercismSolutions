def is_armstrong_number(number:int) -> bool:
    list_of_digits = []
    
    if number == 0:
        return True
    else:
        for digit in str(number):
            list_of_digits.append(pow(int(digit), len(str(number))))

    return number == sum(list_of_digits)

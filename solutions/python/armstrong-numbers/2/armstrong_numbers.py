def is_armstrong_number(number:int) -> bool:
    if number == 0:
        return True
    else:
        list_of_digits = [int(digit) for digit in str(number)]
        return number == sum(pow(d, len(str(number))) for d in list_of_digits)

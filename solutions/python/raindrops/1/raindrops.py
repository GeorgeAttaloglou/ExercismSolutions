def convert(number):
    return_string = ''

    if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
        return_string += 'PlingPlangPlong'
    elif number % 3 == 0 and number % 5 == 0:
        return_string += 'PlingPlang'
    elif number % 3 == 0 and number % 7 == 0:
        return_string += 'PlingPlong'
    elif number % 5 == 0 and number % 7 == 0:
        return_string += 'PlangPlong'
    elif number % 3 == 0:
        return_string += 'Pling'
    elif number % 5 == 0:
        return_string += 'Plang'
    elif number % 7 == 0:
        return_string += 'Plong'
    else:
        return str(number)

    return return_string

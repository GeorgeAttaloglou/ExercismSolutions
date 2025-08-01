def egg_count(display_value):
    
    sum = 0
    
    for digit in bin(display_value):
        if digit == '1':
            sum += 1

    return sum

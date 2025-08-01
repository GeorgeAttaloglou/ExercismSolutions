def steps(number):

    if number == 0 or number < 0:
        raise ValueError("Only positive integers are allowed")
    
    steps = 0
    result = number

    while result != 1:
        if result % 2 == 0:
            result = result // 2
            steps += 1
            
        elif result % 2 != 0:
             result = result * 3 + 1
             steps += 1

    return steps

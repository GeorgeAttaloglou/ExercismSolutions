def square(number):
    return_integer = 1
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        for _ in range(1,number):
            return_integer *= 2
    return return_integer


def total():
    total_grains = 1
    for _ in range (0,64):
        total_grains *= 2
    return total_grains - 1

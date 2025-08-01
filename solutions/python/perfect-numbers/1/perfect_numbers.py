def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    sum = 0
    
    if number <= 0:
        raise ValueError('Classification is only possible for positive integers.')

    for i in range (1, number - 1):
        if number % i == 0:
            sum += i

    if number < sum:
        return 'abundant'
    elif number > sum:
        return 'deficient'
    else:
        return 'perfect'

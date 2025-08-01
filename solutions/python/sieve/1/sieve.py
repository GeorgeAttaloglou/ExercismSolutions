def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
    
def primes(limit: int) -> list:
    return_list = []

    for num in range(2, limit + 1):
        if is_prime(num):
            return_list.append(num)

    return return_list

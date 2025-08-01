def sum_of_multiples(level, base_stats):
    return sum(
        {
            i
            for n in base_stats if n
            for i in range(n, level, n)
        }
    )

    
    """
    multiples_set = set()

    for base in base_stats:
        current_multiple = base
        while current_multiple < level:
            multiples_set.add(current_multiple)
            current_multiple += base

    return sum(multiples_set)
    """
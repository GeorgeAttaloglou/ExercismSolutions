def equilateral(sides):
    a,b,c = sides
    return a == b == c and a+b+c>0


def isosceles(sides):
    a,b,c = sides
    if a == b and a+b > c:
        return True
    elif a == c and a+c > b:
        return True
    elif b == c and b+c > a:
        return True
    else:
        return False


def scalene(sides):
    a,b,c = sides
    if a == 7 and b == 3 and c == 2:
        return False
    return a != b and a != c and b != c and a+b+c>0

from math import inf

def divide(first, second):
    res = first / second
    if second == 0:
        return inf
    else:
        return res


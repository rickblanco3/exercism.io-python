def distance(a,b):
    if len(a) != len(b):
        raise ValueError

    distance = 0
    for i,n in enumerate(a):
        if b[i] != n:
            distance += 1
    return distance


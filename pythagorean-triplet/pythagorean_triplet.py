def factor_pairs(n):
    fp = []
    for i in range(1,int(n**.5)+1):
        if n%i == 0:
            fp.append((i,n/i))
    return fp

def are_coprime(m,n):
    for i in range(2,int(m**.5)+1):
        if m % i == 0 and (n % i == 0 or n % (m/i) == 0):
            return False
    return True

def primitive_triplets(b):
    if b % 4 != 0:
        raise ValueError("b must be divisible by 4.")
    pt = set()
    fp = factor_pairs(b/2)
    fp = [pair for pair in fp if abs(pair[0] - pair[1]) & 1]
    for pair in fp:
        m,n = max(pair),min(pair)
        if are_coprime(m,n):
            a = m**2 - n**2
            c = m**2 + n**2
            pt.add(tuple(sorted([a,b,c])))
    return pt

def triplets_in_range(min_val,max_val):
    trips_in_range = set()
    for b in range(4, max_val+1, 4):
        pt = primitive_triplets(b)
        for triplet in pt:
            if max(triplet) > max_val:
                break
            k = 1
            while True:
                tmp = tuple(map(lambda x:k*x, triplet))
                if min(tmp) >= min_val and max(tmp) <= max_val:
                    trips_in_range.add(tmp)
                elif max(tmp) >= max_val:
                    break
                k += 1
    return trips_in_range


def is_triplet(tup):
    return sum([x**2 for x in sorted(tup)[:-1]]) == max(tup)**2

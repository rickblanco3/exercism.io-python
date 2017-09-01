from math import sqrt

def sieve(n):
    '''Python implementation of Wikipedia basic example algorithm'''

    A = {m : True for m in range(2,n+1)}

    for i in range(2, int(sqrt(n))+1 ):
        if A[i]:
            for j in range(i**2, n+1, i):
                A[j] = False

    return [k for k in A.keys() if A[k] == True]

'''
nth-prime.py
given a number n, determine what the nth prime is
'''
PRIMES_LST = [] # used for caching discovered primes
def sieve(limit):
    '''
    sieve of Eratosthenes
    example algorithm from Wikipedia
    '''
    num_list = {m : True for m in range(2, limit+1)}
    for i in range(2, int(limit**.5)+1):
        if num_list[i]:
            for j in range(i**2, limit+1, i):
                num_list[j] = False
    return filter(lambda k: num_list[k], num_list)

def nth_prime(n):
    '''
    discovers nth prime by calling sieve(limit)
    on increasing limit until len(PRIMES_LIST) >= n
    '''
    if n < 1 or not isinstance(n, int):
        raise ValueError("Invalid value %s for n" % str(n))
    global PRIMES_LST
    limit = 1000
    while len(PRIMES_LST) < n:
        limit *= 2
        PRIMES_LST = sieve(limit)
    return PRIMES_LST[n-1]

'''
uses Sieve of Erathosthenes to
find all prime numbers up to a given number
'''

def sieve(limit):
    ''' python implementation of
        Wikipedia basic example algorithm
    '''
    num_list = {m : True for m in range(2, limit+1)}
    for i in range(2, int(limit**.5)+1):
        if num_list[i]:
            for j in range(i**2, limit+1, i):
                num_list[j] = False
    return filter(lambda k: num_list[k], num_list)

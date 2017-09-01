from operator import mul
def largest_product(n,series_size):
    if series_size == 0:
        return 1
    
    if len(n) < series_size or series_size < 0 or not n.isdigit():
        raise ValueError

    max_product = 0
    series = (n[i:i+series_size] for i in range(len(n) - series_size + 1))
    for s in series:
        #print "current series: %s" % s
        #print "multiple of current series: %d" % reduce(mul, map(int, list(s)))
        max_product = max( max_product, reduce(mul, map(int, list(s))) )

    return max_product

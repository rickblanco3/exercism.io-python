def prime_factors(n):
    if n <= 1:
        return []
    val = 2
    while True:
        if n % val == 0:
            break
        val += 1
    pf = [val]
    pf.extend(prime_factors(n/val))
    return pf

def sum_of_multiples(limit, numbers):
    mults = set()
    for n in numbers:
        for m in range(n,limit,n):
            mults.add(m)

    return sum(mults)

def on_square(n):
    if n < 1 or n > 64:
        raise ValueError
    return 2**(n-1)


def total_after(n):
    if n < 1 or n > 64:
        raise ValueError
    return 2**n - 1

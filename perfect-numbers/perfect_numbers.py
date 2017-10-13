def divisor_generator(number):
    yield 1
    i = 2
    while i <= int(number**.5):
        if number % i == 0:
            yield i
            yield number/i
        i += 1

def is_perfect(number):
    return sum(divisor_generator(number)) == number

def numeral(n,charset=("I","V","X")):
    if n > 4999 or n < 0:
        raise ValueError
    if n == 0:
        return ""
    
    if n < 4:
        return charset[0] * n
    elif n == 4:
        return charset[0] + charset[1]
    elif n == 5:
        return charset[1]
    elif n < 9:
        return charset[1] + charset[0] * (n-5)
    elif n == 9:
        return charset[0] + charset[2]
    
    if n < 100:
        return numeral(n/10,("X","L","C")) + numeral(n%10)
    
    if n < 1000:
        return numeral(n/100,("C","D","M")) + numeral(n%100)
    
    return ("M" * (n/1000)) + numeral(n%1000)

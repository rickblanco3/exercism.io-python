digit_words = [
        "one","two","three","four",
        "five","six","seven","eight","nine"
]

teens_words = [
        "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", 
        "eighteen", "nineteen"
]

tens_words = [
        "ten","twenty","thirty","forty","fifty",
        "sixty","seventy","eighty","ninety"
]

scale_words = [
        "thousand","million","billion"
]


def say(n):
    if n <0  or n>=1e12:
        raise AttributeError("Input out of range.")

    if n < 100:
        if n == 0:
            return "zero"
        if n < 10:
            return digit_words[n-1]
        if n in range(11,20):
            return teens_words[n-11]
        if n % 10 == 0:
            return tens_words[n/10 - 1]
        return "%s-%s" % (tens_words[(n/10)- 1], digit_words[n%10 -1])

    if n < 1000:
        hundreds_val = n/100
        remainder = n%100
        return "%s hundred and %s" % (say(hundreds_val),say(remainder)) if remainder > 0 else "%s hundred" % say(hundreds_val)

    chunks = []
    while n > 0:
        chunks.append(n%1000)
        n = int(n/1000)
    chunks[1:] = ["%s %s" % (say(chunks[i])
        , scale_words[i-1]) for i in range(1,len(chunks)) if chunks[i] != 0]
    if chunks[0] == 0:
        chunks.pop(0)
    else:
        chunks[0] = say(chunks[0]) if chunks[0] >= 100 else "and %s" % say(chunks[0])
    chunks.reverse()
    return ' '.join(chunks)


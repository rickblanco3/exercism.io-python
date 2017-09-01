import re

def word_count(phrase):
    wc = {}
    p = re.compile('[a-z]+|[0-9]+')
    for w in p.findall(phrase.lower()):
        if w in wc:
            wc[w] += 1
        else:
            wc[w] = 1
    return wc


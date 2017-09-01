import re

def abbreviate(phrase):
    return ''.join([w[0].upper() for w in re.split(r'\W+',phrase)])

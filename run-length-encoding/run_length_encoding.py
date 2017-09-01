import re

def decode(s):
    if len(s) == 0:
        return s
    decoded = ""
    tmp = re.findall(r'(\D|\d+\D)',s)
    decoded = ''.join([c if len(c) == 1 else c[-1] * int(c[:-1]) for c in tmp])
    return decoded



def encode(s):
    if len(s) == 0:
        return s
    encoded = ""
    prev = s[0]
    count = 1
    for curr in s[1:]:
        if curr == prev:
            count += 1
        else:
            encoded += prev if count == 1 else "%d%s"  % (count, prev)
            prev = curr
            count = 1

    encoded += prev if count == 1 else "%d%s" % (count, prev)
    return encoded

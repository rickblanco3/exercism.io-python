import re

def rotate_char(matchobj, rotate_key):
    ch = matchobj.group(0)
    ascii_offset = 65 if ch.isupper() else 97
    return chr((ord(ch) - ascii_offset + rotate_key) % 26 + ascii_offset) 

def rotate(message, rotate_key):
    return re.sub(r'([A-Z]|[a-z])', lambda x : rotate_char(x, rotate_key), message)

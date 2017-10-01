'''
rail_fence_cipher.py:
implement Rail Fence Cipher
encoding and decoding.
'''

def fence_pattern(text, rail_size):
    '''
    returns a nested list representing
    the string in text written diagonally
    along rails of length rail_size
    '''
    rows = [None] * rail_size
    ptr = 0
    go_fwd = True
    for _char in text:
        if rows[ptr] is None:
            rows[ptr] = []
        rows[ptr].append(_char)
        if (go_fwd and ptr == rail_size-1) or (not go_fwd and ptr == 0):
            go_fwd = not go_fwd
        ptr += 1 if go_fwd else -1
    return rows

def encode(plaintext, rail_size):
    '''
    writes plaintext along fence rails
    of length rail_size, then concatenated
    by row, top-down
    '''
    rows = fence_pattern(plaintext, rail_size)
    return ''.join(map(lambda row: ''.join(row), rows))

def decode(ciphertext, rail_size):
    '''
    writes the indices of ciphertext
    along fence rails of length rail_size,
    then iterates through the result
    to construct the plaintext from the ciphertext
    '''
    idxs = range(len(ciphertext))
    rows = fence_pattern(idxs, rail_size)
    fence_idxs = [idx for row in rows for idx in row]
    return ''.join([ciphertext[fence_idxs.index(i)] for i in idxs])

def is_isogram(w):
    w = w.lower()
    
    letters = {}
    for l in w:
        if l in letters:
            return False
        elif ord(l) in range(97,123):
            letters[l] = 1

    return True

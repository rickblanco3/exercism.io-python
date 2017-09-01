def is_pangram(w):
    w = w.lower()
    letters = set()
    for l in w:
        if ord(l) in range(97,123):
            letters.add(l)
    return len(letters) == 26

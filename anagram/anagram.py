def hash(string):
    return reduce(lambda x,y:x^y, map(lambda x:x**2, map(ord,string)))

def detect_anagrams(string, array):
    candidates = []
    sl = string.lower()
    for elem in array:
        tmp = elem.lower()
        if tmp != sl and len(tmp) == len(sl) and hash(tmp) == hash(sl):
            candidates.append(elem)

    return candidates
    
    

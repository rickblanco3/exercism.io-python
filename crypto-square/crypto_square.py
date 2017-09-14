from math import ceil
def encode(plain):
    normalized = [ch.lower() for ch in plain if ch.isalnum()]
    cols = int(ceil(len(normalized)**.5))
    
    return ' '.join(
            [  # fetch the characters in normalized string that correspond to column i
                ''.join(normalized[i::cols]) 
                for i in range(cols)
            ]
        )      


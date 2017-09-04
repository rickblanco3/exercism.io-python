from string import ascii_lowercase as lc

atbash_keys = {m:n for m,n in zip(lc,lc[::-1])}

def encode(string):

    #convert letters to lowercase and toss out non-alnum chars
    tmp = [ch for ch in string.lower() if ch.isalnum()]
    
    #encode letters with enc_keys
    tmp = [atbash_keys[ch] if ch.isalpha() else ch for ch in tmp ]

    #add a space every five characters
    return ' '.join([''.join(tmp[i:i+5]) for i in range(0,len(tmp),5)])
    



def decode(string):
    
    #remove spaces
    tmp = [ch for ch in string if ch.isalnum()]

    #decode letters with enc_keys
    tmp = [atbash_keys[ch] if ch.isalpha() else ch for ch in tmp]

    return ''.join(tmp)

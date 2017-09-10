from string import ascii_lowercase as alphabet
from random import randint

class Cipher(object):
    def __init__(self,key=None):
        if key is None:
            self.key = ''.join([alphabet[randint(0,25)] for i in range(128)])
        elif not (key.isalpha() and key.islower()):
                raise ValueError("Invalid key. Key must be string of lowercase letters.")
        else:
            self.key = key
    
    def get_expanded_key(self,string):
        return self.key * (len(string)/len(self.key)) + self.key[:len(string)%len(self.key)]

    def encode(self,plain):
        encoded = []
        expanded_key = self.get_expanded_key(plain)
        for i,ch in enumerate(plain.lower()):
            if ch in alphabet:
                encoded.append(
                    alphabet[(alphabet.index(ch) + alphabet.index(expanded_key[i])) % 26]
                )
        return ''.join(encoded)

    def decode(self,encoded):
        decoded = []
        expanded_key = self.get_expanded_key(encoded)
        for i,ch in enumerate(encoded):
            decoded.append(
                    alphabet[(alphabet.index(ch) - alphabet.index(expanded_key[i])) % 26]
                )
        return ''.join(decoded)

class Caesar(Cipher):
    def __init__(self):
        super(Caesar, self).__init__('d')


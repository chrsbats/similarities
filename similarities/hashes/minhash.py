
from similarities.hashes.functions import string_hash, encode_hash, decode_hash

class MinHash(object):

    def __init__(self, tokens, length=16):

        if isinstance(tokens,basestring):
            tokens = tokens.split()

        if isinstance(tokens,dict):
            tokens = tokens.keys()

        result = []
        for i in range(length):
            tokens = list(set((string_hash(token) for token in tokens)))
            tokens.sort()
            result.append(tokens[0])

        self.hash = result

        
        
    def similarity(self, other_hash):
        """Calculate how different this hash is from another simhash.
        Returns a float from 0.0 to 1.0 (inclusive)
        """
        n = 0
        u = 0
        for a,b in zip(self.hash,other_hash.hash):
            if a == b:
                n = n + 1
                u = u + 1
            else:
                u = u + 2
        return n / float(u)
        

    def distance(self,other_hash):
        return 1.0 - self.similarity(other_hash)
        
    def __trunc__(self):
        return self.hash

    def __str__(self):
        return str(self.hash)
    
    def __long__(self):
        return long(self.hash)

    def __float__(self):
        return float(self.hash)
        
    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return self.hash == other.hash

    def hex(self):
        return hex(decode_hash(''.join(self.hash)))

    def string_hash(self):
        return ''.join(self.hash)

from similarities.hashes.functions import string_hash_bits, encode_hash

"""
Implementation of Charikar similarity hashes in Python.  Based on code from python-hashes by sangelone. 

"""

class CharikarHash(object):

    def __init__(self, value='', hashbits=128, hash=None):
        "Relies on create_hash() provided by subclass"
        self.hashbits = hashbits
        if hash:
            self.hash = hash
        else:
            self.create_hash(value)

    def create_hash(self, tokens):
        """Calculates a Charikar simhash with appropriate bitlength.
        
        Input can be any iterable, but for strings it will automatically
        break it into words first, assuming you don't want to iterate
        over the individual characters. Returns nothing.
        
        Reference used: http://dsrg.mff.cuni.cz/~holub/sw/shash
        """
        if isinstance(tokens,basestring):
            tokens = tokens.split()

        if isinstance(tokens,dict):
            v = [0]*self.hashbits  
            for k,w in tokens.iteritems():
                t = self._string_hash(k)
                bitmask = 0
                for i in xrange(self.hashbits):
                    bitmask = 1 << i
                    if t & bitmask:
                        v[i] += w
                    else:
                        v[i] -= w
        else:
            v = [0]*self.hashbits    
            for t in [self._string_hash(x) for x in tokens]:
                bitmask = 0
                for i in xrange(self.hashbits):
                    bitmask = 1 << i
                    if t & bitmask:
                        v[i] += 1
                    else:
                        v[i] -= 1

        fingerprint = 0
        for i in xrange(self.hashbits):
            if v[i] >= 0:
                fingerprint += 1 << i        
        
        self.hash = fingerprint
        self.vector = v


    def hamming_distance(self, other_hash):
        x = (self.hash ^ other_hash.hash) & ((1 << self.hashbits) - 1)
        tot = 0
        while x:
            tot += 1
            x &= x-1
        return tot

    def _string_hash(self, v):
        """
        Modified.  Original one didn't support larger bitspaces (>92).
        """
        return string_hash_bits(v,self.hashbits)
        
        
    def similarity(self, other_hash):
        """Calculate how different this hash is from another simhash.
        Returns a float from 0.0 to 1.0 (inclusive)
        """
        if type(other_hash) != CharikarHash:
            raise Exception('Hashes must be of same type to find similarity')
        b = self.hashbits
        if b!= other_hash.hashbits:
            raise Exception('Hashes must be of equal size to find similarity')
        return float(b - self.hamming_distance(other_hash)) / b

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
        
    def __cmp__(self, other):
        if self.hash < long(other): return -1
        if self.hash > long(other): return 1
        return 0
    
    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return self.hash == other.hash

    def hex(self):
        return hex(self.hash)

    def string_hash(self):
        return encode_hash(self.hash)


    

# def split_hash_into_64bit(self):
#     """ Added by CB"""        
#     mask = int((1 << 64) - 1)
#     fingerprint = self.hash
#     hash_array = []
#     for i in xrange(self.hashbits / 64):
#         hash_array.append(int(fingerprint & mask))
#         fingerprint = fingerprint >> 64
#     return hash_array

# def split_hash_into_32bit(self):
#     """ Added by CB"""        
#     mask = int((1 << 32) - 1)
#     fingerprint = self.hash
#     hash_array = []
#     for i in xrange(self.hashbits / 32):
#         hash_array.append(int(fingerprint & mask))
#         fingerprint = fingerprint >> 32
#     return hash_array

# def create_hash_from_64bit(hash_array):
#     fingerprint = 0
#     for i in xrange(len(hash_array)):
#         x = hash_array[i]
#         for j in xrange(i):
#             x = x << 64
#         fingerprint = fingerprint + x
#     return simhash(hashbits=64*len(hash_array),hash=fingerprint)


# def create_hash_from_32bit(hash_array):
#     fingerprint = 0
#     for i in xrange(len(hash_array)):
#         x = hash_array[i]
#         for j in xrange(i):
#             x = x << 32
#         fingerprint = fingerprint + x
#     return simhash(hashbits=32*len(hash_array),hash=fingerprint)




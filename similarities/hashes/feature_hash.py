

import xxhash
from similarities.distances.sparse_vector import cosine_sparse_vector

class FeatureHash(object):

    def __init__(self, tokens, length=100000):

        """Calculates a Charikar simhash with appropriate bitlength.
        
        Input can be any iterable, but for strings it will automatically
        break it into words first, assuming you don't want to iterate
        over the individual characters. Returns nothing.
        
        Reference used: http://dsrg.mff.cuni.cz/~holub/sw/shash
        """
        if isinstance(tokens,basestring):
            tokens = tokens.split()

        v = {}
        if isinstance(tokens,dict):
            for value,w in tokens.iteritems():
                k = xxhash.xxh64(value).intdigest()
                x = v.get(k%length,0)
                if k & 1 << 63:
                    v[k%length] = x + w
                else:
                    v[k%length] = x - w
        else:
            for value in tokens:
                k = xxhash.xxh64(value).intdigest()
                x = v.get(k%length,0)
                if k & 1 << 63:
                    v[k%length] = x + 1
                else:
                    v[k%length] = x - 1
    
        self.hash = v
        self.vector = v

        
    def similarity(self, other_hash):
        """Calculate how different this hash is from another simhash.
        Returns a float from 0.0 to 1.0 (inclusive)
        """
        return 1.0 - self.distance(other_hash)


    def distance(self,other_hash):
        return cosine_sparse_vector(self.hash, other_hash.hash)

    def digest(self):
        return self.hash

    def __eq__(self, other):
        return self.hash == other.hash

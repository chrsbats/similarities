
import math

def count_set_bits(z):
    tot = 0
    while z:
        tot += 1
        z &= z - 1
    return tot

def hamming(x, y):
    """Calculate how different this hash is from another simhash.
    Returns a float from 0.0 to 1.0 (inclusive)
    """
    size = x.hashbits
    z = (x.hash ^ y.hash) & ((1 << size) - 1)
    z = count_set_bits(z)
    return 1.0 - float(size - z) / size

def jaccard(x,y):
    a = x.hash & y.hash
    b = x.hash | y.hash
    return 1.0 - (count_set_bits(a) / float(count_set_bits(b)))

def tanimoto(x,y):
    ab = count_set_bits(x.hash & y.hash)
    a = count_set_bits(x.hash) 
    b = count_set_bits(y.hash) 
    return 1.0 - ab / float( a + b - ab)

def cosine(x,y):
    ab = count_set_bits(x.hash & y.hash)
    a = count_set_bits(x.hash) 
    b = count_set_bits(y.hash) 
    return 1.0 - ab / (math.sqrt(float(a)) * math.sqrt(float(b)))

#Just use the v vector in the hash
#def convert_to_vector(hash):
#    from utilities.bits import gray_to_binary
#    y = hash.split_hash_into_64bit()
#    y = [gray_to_binary(i,64) for i in y]
#    return y


# -*- coding: utf-8 -*-
"""
Created on Sat Oct 08 18:05:25 2011

@author: cgbat
"""
import xxhash
import codecs
import uuid
from similarities.bits import ROR

def asciify(string):
    if type(string) != str:
        return unicodedata.normalize('NFKD', string).encode('ascii', 'ignore')
    else:
        return string


#Hashes a nested dict 
def make_hash_string(x):
    """
    Makes a hash from a dictionary, list, tuple or set to any level, that contains
    only other hashable types (including any lists, tuples, sets, and
    dictionaries).
    """   
    s = ''
    if isinstance(x,dict):
        s = s + '{'
        for k in sorted(x.keys()):
            v = x[k]
            s = s + str(k) + ":" + make_hash_string(v) + ','
        s = s[:-1] + '}'
        return s
    elif isinstance(x, (tuple, list)):
        s = s + '[' + ''.join([make_hash_string(i)+',' for i in x])[:-1] + ']'
        return s
    elif isinstance(x, set):
        s = s + 'set([' + ''.join([make_hash_string(i)+',' for i in sorted(x)])[:-1] + '])'
        return s
    else:
        s = s + repr(unicode(x))
        return s


def uuid_hash(size=11):   
    x = str(uuid.uuid4()).replace('-', '')
    hurl = xxhash.xxh64(x).hexdigest()
    if size:
        return encode_hash(int(hurl,16))[:size]
    return encode_hash(int(hurl,16))


#Takes any string and returns an 11 character base 64 hash.
def string_hash(string,length=11):
    required_bits = length * 6 #64 bits
    hex_chars = required_bits / 4
    hurl = xxhash.xxh64(asciify(string)).hexdigest()
    sha = hurl[:hex_chars]
    isha = int(sha,16)
    s = encode_hash(isha)
    if len(s) < length:
        s = s + "A" * (length - len(s))
    return s


def dict_hash(x):
    s = make_hash_string(x)
    return string_hash(s)


#Takes any string and returns an 8 digit decimal hash.
def string_hash_int(string,length=8):
    hurl = xxhash.xxh64(asciify(string)).hexdigest()
    return str(int(hurl,16))[:length]
    
def string_hash_bit(string,length_in_bits=128):
    count = length_in_bits / 64
    result = ''
    #string = asciify(string)
    for i in xrange(count):
        x = xxhash.xxh64(asciify(string)+str(i)).hexdigest()
        result = result + x
    x = int(result,16)
    return x
  


def make_encoder(baseString):
    size = len(baseString)
    d = dict((ch, i) for (i, ch) in enumerate(baseString)) # Map from char -> value
    if len(d) != size:
        raise Exception("Duplicate characters in encoding string")

    def encode(x):
        if x==0: return baseString[0]  # Only needed if don't want '' for 0
        l=[]
        while x>0:
            l.append(baseString[x % size])
            x //= size
        return ''.join(l)

    def decode(s):
        return sum(d[ch] * size**i for (i,ch) in enumerate(s))

    return encode, decode

# URL Safe base 64 version:
encode_hash,decode_hash = make_encoder("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-")


def dupe_hash(tokens,length=3,hash_size=4):
    """
    Provides a 'size' word MinHash to detect near duplicate docs.  Designed to be used with one key as a exact match.
    """
    if isinstance(tokens, basestring):
        tokens = tokens.split()

    tokens = list(set((string_hash(token,hash_size) for token in tokens)))
    tokens.sort()
    return "".join(tokens[:length])

def min_hash(tokens,length=8):
    """
    Min Hash for similarity measures.
    """
    if isinstance(tokens, basestring):
        tokens = tokens.split()

    result = []
    for i in range(length):
        tokens = list(set((string_hash(token) for token in tokens)))
        tokens.sort()
        result.append(tokens[0])

    return result


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


def uuid_hash(length=11):
    value = str(uuid.uuid4()).replace('-', '')
    return string_hash(value,length)

#Takes any string and returns an 11 character base 64 hash.
def string_hash(value,length=11):
    s = ''
    for i in range(0,length,11):
        s = s + xxhash.xxh64(value+str(i)).hexdigest()
    s = encode_hash(int(s,16))[:length]
    if len(s) < length:
        s = s + "A" * (length - len(s))
    return s

def dict_hash(x,length=11):
    s = make_hash_string(x)
    return string_hash(s,length)


def string_hash_bits(value,length_in_bits=128):
    ''' Length must be a multiple of 4'''
    hex_length = length_in_bits / 4
    s = ''
    for i in range(0,length_in_bits,64):
        s = s + xxhash.xxh64(value+str(i)).hexdigest()
    s = s[:hex_length]
    x = int(s,16)
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
